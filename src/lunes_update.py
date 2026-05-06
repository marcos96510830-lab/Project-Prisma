import subprocess

def lunes_check_and_update():
    print("=== LUNES: AGENTE DE ATUALIZAÇÃO E SEGURANÇA ===")
    print("[✓] Lunes ativado e operando sob diretrizes éticas.\n")
    
    resposta = input("Deseja verificar e atualizar os pacotes do sistema? (Y/n): ").strip().lower()
    
    if resposta == 'y' or resposta == '':
        print("\n[+] Lunes está executando o update do sistema...")
        subprocess.run("yes | pkg update && yes | pkg upgrade", shell=True)
        print("\n[✓] Sistema de pacotes atualizado com sucesso!")
    else:
        print("\n[-] Lunes: Atualização de pacotes ignorada.")
        
    print("\n=== LUNES: OPERAÇÃO CONCLUÍDA ===")

if __name__ == "__main__":
    lunes_check_and_update()

