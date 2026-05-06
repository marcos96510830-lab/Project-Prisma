import os
import time
from datetime import datetime

# Simulação simples de criptografia (substituível por bibliotecas como cryptography)
def criptografar_dado(texto):
    # Deslocamento simples de cifra para exemplo didático
    return "".join([chr(ord(c) + 3) for c in texto])

def registrar_log(operacao, status="INFO"):
    arquivo = "prisma_audit.log"
    tempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    linha = f"[{tempo}] {status.upper()} - OPERACAO: {operacao}"
    linha_cripto = criptografar_dado(linha)
    
    with open(arquivo, "a") as f:
        f.write(linha_cripto + "\n")
        
    print(f"[LOG] Registro auditado e protegido com sucesso.")

if __name__ == "__main__":
    registrar_log("Teste de inicialização do sistema de auditoria", "INFO")

