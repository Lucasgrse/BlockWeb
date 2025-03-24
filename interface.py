import tkinter as tk
from tkinter import messagebox
from service import BlockSitesService

class BlockSitesApp:
    def __init__(self, root, service):
        self.root = root
        self.service = service
        self.root.title("Bloqueador de Sites")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Bloqueador de Sites", font=("Arial", 20))
        self.title_label.pack(pady=10)
        
        self.site_entry = tk.Entry(self.root, width=40)
        self.site_entry.pack(pady=5)
        
        self.add_button = tk.Button(self.root, text="Adicionar Site", command=self.add_site)
        self.add_button.pack(pady=5)
        
        self.sites_listbox = tk.Listbox(self.root, width=40, height=10)
        self.sites_listbox.pack(pady=10)
        
        self.remove_button = tk.Button(self.root, text="Remover Site", command=self.remove_site)
        self.remove_button.pack(pady=5)

        self.block_button = tk.Button(self.root, text="Bloquear Sites", command=self.block_sites_in_hosts)
        self.block_button.pack(pady=5)

        self.unblock_button = tk.Button(self.root, text="Desbloquear Sites", command=self.unblock_sites)
        self.unblock_button.pack(pady=5)

    def add_site(self):
        site = self.site_entry.get().strip()
        if site and site not in self.service.block_sites:
            self.service.add_site(site)
            self.sites_listbox.insert(tk.END, site)
            self.site_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Este site já está na lista ou não é válido.")

    def remove_site(self):
        selected_site = self.sites_listbox.curselection()
        if selected_site:
            site = self.sites_listbox.get(selected_site)
            self.service.remove_site(site)
            self.sites_listbox.delete(selected_site)
        else:
            messagebox.showwarning("Aviso", "Selecione um site para remover.")

    def block_sites_in_hosts(self):
        # Bloqueia os sites
        self.service.block_sites_in_hosts()
        self.update_sites_listbox()     
        messagebox.showinfo("Sucesso", "Sites bloqueados com sucesso.")

    def unblock_sites(self):
        # Desbloqueia os sites
        self.service.unblock_sites()
        self.update_sites_listbox()
        messagebox.showinfo("Sucesso", "Sites desbloqueados com sucesso.")

    def update_sites_listbox(self):
        self.sites_listbox.delete(0, tk.END)
        
        for site in self.service.block_sites:
            self.sites_listbox.insert(tk.END, site)

def run_app():
    service = BlockSitesService()
    root = tk.Tk()
    app = BlockSitesApp(root, service)
    root.mainloop()

if __name__ == "__main__":
    run_app()