import os

# Caminho para o arquivo hosts no Windows
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# IP local para redirecionar os sites bloqueados
redirect_ip = "127.0.0.1"

class BlockSitesService:
    def __init__(self):
        self.block_sites = []

    def add_site(self, site):
        """Adiciona um site à lista de sites bloqueados."""
        if site not in self.block_sites:
            self.block_sites.append(site)

    def remove_site(self, site):
        """Remove um site da lista de sites bloqueados."""
        if site in self.block_sites:
            self.block_sites.remove(site)

    def block_sites_in_hosts(self):
        """Bloqueia os sites no arquivo hosts."""
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in self.block_sites:
                # Limpeza do domínio
                clean_site = site.replace("http://", "").replace("https://", "").strip()
                # Verificar se já existe no arquivo
                if f"{redirect_ip} {clean_site}" not in content:
                    file.write(f"\n{redirect_ip} {clean_site}\n")
        print("Sites bloqueados com sucesso.")

    def unblock_sites(self):
        """Desbloqueia os sites removendo-os do arquivo hosts."""
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in self.block_sites):
                    file.write(line)
            file.truncate()
        print("Sites desbloqueados com sucesso.")
