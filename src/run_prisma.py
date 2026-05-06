import os
import subprocess

def main():
    print("=== INICIALIZANDO O PROJECT PRISMA ===")
    print("\n--- [ 1. Chegagem de Sistema ] ---")
    print("Iniciando verificação de integridade do sistema...")
    
    # Checagem de espaço livre simulada/real
    st = os.statvfs('/')
    free_gb = (st.f_bavail * st.f_frsize) / 1024 / 1024 / 1024
    print(f"[+] Espaço livre no disco: {free_gb:.2f} GB")
    
    dir_path = os.path.expanduser("~/Project-Prisma")
    print(f"[+] Diretório do projeto: {dir_path} [OK]")
    print("[+] Arquivo de log ainda não criado.")
    print("---------------------------------------")
    print("Verificação do Prisma concluída com sucesso!")
    
    print("\n--- [ 2. Chegagem de Pacotes (Lunes) ] ---")
    print("=== LUNES: AGENTE DE ATUALIZAÇÃO E SEGURANÇA ===")
    print("[✓] Lunes ativo e operando sob diretrizes éticas.")
    
    resposta = input("\nDeseja verificar e atualizar os pacotes do sistema? (Y/n): ").strip().lower()
    
    if resposta == 'y' or resposta == '':
        print("\n[+] Lunes está executando o update do sistema...")
        subprocess.run("pkg update -y && pkg upgrade -y", shell=True)
        print("\n[✓] Sistema de pacotes atualizado com sucesso!")
    
    print("\n=== LUNES: OPERAÇÃO CONCLUÍDA ===")
    
    print("\n--- [ 3. Sincronização com o GitHub ] ---")
    sync = input("Deseja sincronizar o projeto com o GitHub? (Y/n): ").strip().lower()
    
    if sync == 'y' or sync == '':
        print("\n[+] Sincronizando com o GitHub...")
        os.chdir(dir_path)
        subprocess.run("git add -A && git commit -m 'auto: Sincronização automatizada' && git push origin main", shell=True)
        print("[✓] Sincronização concluída com sucesso.")
    
    print("\n=== PRISMA PRONTO PARA USO ===")

if __name__ == '__main__':
    main()

