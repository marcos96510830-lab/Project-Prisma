import os
import time
import subprocess
from logs_manager import registrar_log
from recon_scanner import escanear_alvo

def check_identity():
    result = subprocess.getoutput("proxychains4 curl -s https://check.torproject.org/api/ip")
    return '"IsTor":true' in result

def monitorar_vazamento():
    print("\n" + "═"*40)
    print(" [PRISMA] MODO VIGILÂNCIA (KILL SWITCH) ")
    print("═"*40)
    print("[*] Escaneando túnel... Pressione Ctrl+C para parar.")
    registrar_log("Monitoramento de vigilância iniciado", "INFO")
    
    try:
        while True:
            if check_identity():
                print("[OK] Identidade protegida.           ", end="\r")
            else:
                print("\n[!!!] ALERTA: VAZAMENTO DETECTADO!")
                os.system("service tor stop")
                os.system("pkill -9 tor")
                registrar_log("Vazamento de IP detectado - Conexão cortada", "CRITICAL")
                break
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[*] Vigilância encerrada.")
        registrar_log("Vigilância encerrada pelo usuário", "INFO")

def menu_prisma():
    while True:
        print("\n" + "─"*30)
        print("    NEXUS - MÓDULO PRISMA")
        print("─"*30)
        print("1. Verificar IP Atual (Onion)")
        print("2. Ativar Kill Switch (Vigilância)")
        print("3. Testar Conexão Externa (Curl)")
        print("4. Chamar Net Guard (Lunes)")
        print("5. Ver Logs de Auditoria")
        print("6. Iniciar Reconhecimento (Auditoria)")
        print("7. Sair")
        
        escolha = input("\nPrisma > ")
        
        if escolha == "1":
            status = subprocess.getoutput("proxychains4 curl -s https://check.torproject.org/api/ip")
            print(f"\n[Status]: {status}")
            registrar_log("Consulta de IP realizada", "INFO")
        elif escolha == "2":
            monitorar_vazamento()
        elif escolha == "3":
            url = input("Digite o site (ex: google.com): ")
            os.system(f"proxychains4 curl -I {url}")
            registrar_log(f"Teste de requisição para {url}", "INFO")
        elif escolha == "4":
            os.system("python3 lunes_net_guard.py")
            registrar_log("Monitoramento de intrusão Lunes acionado", "INFO")
        elif escolha == "5":
            if os.path.exists("prisma_audit.log"):
                with open("prisma_audit.log", "r") as f:
                    conteudo = f.read()
                    print("\n[Logs Criptografados]:\n", conteudo)
            else:
                print("\n[X] Nenhum log encontrado.")
        elif escolha == "6":
            target = input("Digite o domínio alvo de teste (ex: testsite.com): ")
            escanear_alvo(target)
            print("\n[v] Auditoria finalizada. Verifique os logs.")
        elif escolha == "7":
            registrar_log("Sessão encerrada", "INFO")
            break

if __name__ == "__main__":
    menu_prisma()

