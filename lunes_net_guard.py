import os

def verificar_intrusos():
    print("\n" + "═"*40)
    print(" [LUNES] MONITOR DE INTRUSÃO 2.0 ")
    print("═"*40)
    print("[*] Analisando tráfego de rede ativo...")
    os.system("ss -tpn") 
    print("\n[*] Portas abertas aguardando entrada:")
    os.system("ss -lntup")
    print("\n[*] Identidade do Processo Nexus:")
    os.system("id")
    print("═"*40 + "\n")

if __name__ == "__main__":
    verificar_intrusos()

