import os
import time
import subprocess

def check_identity():
    result = subprocess.getoutput("proxychains4 curl -s https://check.torproject.org/api/ip")
    return '"IsTor":true' in result

def monitorar_vazamento():
    print("\n" + "═"*40)
    print(" [PRISMA] MODO VIGILÂNCIA (KILL SWITCH) ")
    print("═"*40)
    print("[*] Escaneando túnel... Pressione Ctrl+C para parar.")
    try:
        while True:
            if check_identity():
                print("[OK] Identidade protegida.           ", end="\r")
            else:
                print("\n[!!!] ALERTA: VAZAMENTO DETECTADO!")
                os.system("service tor stop")
                os.system("pkill -9 tor")
                print("[!] EMERGÊNCIA: Conexão cortada para segurança.")
                break
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[*] Vigilância encerrada.")

def menu_prisma():
    while True:
        print("\n" + "─"*30)
        print("    NEXUS - MÓDULO PRISMA")
        print("─"*30)
        print("1. Verificar IP Atual (Onion)")
        print("2. Ativar Kill Switch (Vigilância)")
        print("3. Testar Conexão Externa (Curl)")
        print("4. Chamar Net Guard (Lunes)")
        print("5. Sair")
        
        escolha = input("\nPrisma > ")
        
        if escolha == "1":
            status = subprocess.getoutput("proxychains4 curl -s https://check.torproject.org/api/ip")
            print(f"\n[Status]: {status}")
        elif escolha == "2":
            monitorar_vazamento()
        elif escolha == "3":
            url = input("Digite o site (ex: google.com): ")
            os.system(f"proxychains4 curl -I {url}")
        elif escolha == "4":
            os.system("python3 lunes_net_guard.py")
        elif escolha == "5":
            break

if __name__ == "__main__":
    menu_prisma()


