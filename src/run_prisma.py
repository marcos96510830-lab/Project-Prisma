import os
import subprocess

def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            print(stdout.decode('utf-8'))
        if stderr:
            print(stderr.decode('utf-8'))
    except Exception as e:
        print(f"Erro ao executar comando: {e}")

def main():
    print("=== INICIALIZANDO O PROJECT PRISMA ===")
    
    # 1. Executar verificação de saúde do sistema
    print("\n--- [ 1. Checagem de Sistema ] ---")
    run_command("python3 ~/Project-Prisma/src/prisma_check.py")
    
    # 2. Atualizar repositório (Git)
    print("\n--- [ 2. Sincronização com GitHub ] ---")
    run_command("git add -A && git commit -m 'auto: Execucao automatica e atualizacao do sistema' && git push origin main")
    
    print("\n=== PRISMA PRONTO PARA USO ===")

if __name__ == "__main__":
    main()

