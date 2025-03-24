import os
import time
import win32serviceutil
import win32service
import win32event
from service import BlockSitesService
import tkinter as tk
from interface import BlockSitesApp

class BlockSitesWindowsService(win32serviceutil.ServiceFramework):
    _svc_name_ = "BlockSitesService"
    _svc_display_name_ = "Bloqueador de Sites"
    _svc_description_ = "Este serviço bloqueia e desbloqueia sites no arquivo hosts."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.service = BlockSitesService()
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        """Método chamado para parar o serviço."""
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
    
    def SvcDoRun(self):
        """Método chamado para rodar o serviço."""
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        
        while True:
            self.service.block_sites_in_hosts()

# Função principal para iniciar o serviço
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(BlockSitesWindowsService)
