import os
import shutil
import time

def raio_x_prisma():
    print("Iniciando verificação de integridade do sistema...")
    print("-" * 45)
    
    # 1. Verificação de armazenamento disponível
    total, usado, livre = shutil.disk_usage("/")
    livre_gb = livre / (1024**3)
    
    print(f"[+] Espaço livre no disco: {livre_gb:.2f} GB")
    
    # 2. Verificação de diretório do projeto
    prisma_dir = os.path.expanduser("~/Project-Prisma")
    if os.path.exists(prisma_dir):
        print(f"[+] Diretório do projeto: {prisma_dir} [OK]")
    else:
        print(f"[!] Diretório não encontrado: {prisma_dir}")

    # 3. Análise de segurança de arquivos
    log_file = os.path.join(prisma_dir, "seguranca.log")
    if os.path.exists(log_file):
        tamanho_log = os.path.getsize(log_file)
        print(f"[+] Arquivo de log verificado. Tamanho: {tamanho_log} bytes")
    else:
        print("[+] Arquivo de log ainda não criado.")
        
    print("-" * 45)
    print("Verificação do Prisma concluída com sucesso!")

if __name__ == "__main__":
    raio_x_prisma()

