import os
import subprocess

def main():
    print("=== INICIALIZANDO O PROJECT PRISMA ===")
    
    # 1. Executar verificação de saúde do sistema (Sem capturar a tela para mostrar interações)
    print("\n--- [ 1. Checagem de Sistema ] ---")
    subprocess.run(["python3", os.path.expanduser("~/Project-Prisma/src/prisma_check.py")])
    
    # 2. Executar o agente Lunes para atualizações
    print("\n--- [ 2. Checagem de Pacotes (Lunes) ] ---")
    subprocess.run(["python3", os.path.expanduser("~/Project-Prisma/src/lunes_update.py")])
    
    # 3. Pergunta interativa para o GitHub
    print("\n--- [ 3. Sincronização com o GitHub ] ---")
    opcao = input("Deseja sincronizar o projeto com o GitHub? (Y/n): ").strip().lower()
    
    if opcao == 'y' or opcao == '':
        print("\n[+] Sincronizando com o GitHub...")
        subprocess.run("git add -A && git commit -m 'auto: Execucao automatica do sistema com Lunes' && git push origin main", shell=True)
        print("[✓] Sincronização concluída com sucesso.")
    else:
        print("\n[-] Sincronização com o GitHub ignorada. Operação apenas local.")
        
    print("\n=== PRISMA PRONTO PARA USO ===")

if __name__ == "__main__":
    main()

