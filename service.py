import os

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"

class BlockSitesService:
    def __init__(self):
        self.block_sites = []

    def add_site(self, site):
        if site not in self.block_sites:
            self.block_sites.append(site)

    def remove_site(self, site):
        if site in self.block_sites:
            self.block_sites.remove(site)

    def block_sites_in_hosts(self):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in self.block_sites:
                clean_site = site.replace("http://", "").replace("https://", "").strip()
                if f"{redirect_ip} {clean_site}" not in content:
                    file.write(f"\n{redirect_ip} {clean_site}\n")
        print("Sites bloqueados com sucesso.")

    def unblock_sites(self):
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in self.block_sites):
                    file.write(line)
            file.truncate()
        print("Site(s) desbloqueado(s) com sucesso.")
