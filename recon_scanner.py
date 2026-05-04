import os
import subprocess
from logs_manager import registrar_log

def escanear_alvo(url_alvo):
    print(f"\n[*] Iniciando reconhecimento em {url_alvo}...")
    registrar_log(f"Início da varredura de segurança no alvo: {url_alvo}", "INFO")
    
    # Lista de diretórios comuns de teste para auditoria ética
    diretorios = ["/admin", "/config.php", "/backup", "/api/v1/users"]
    
    resultados = []
    
    for diretorio in diretorios:
        url_teste = f"http://{url_alvo}{diretorio}"
        # Teste silencioso via proxychains
        comando = f"proxychains4 curl -s -o /dev/null -w '%{{http_code}}' {url_teste}"
        codigo_http = subprocess.getoutput(comando)
        
        if codigo_http in ["200", "403", "301"]:
            resultados.append((diretorio, codigo_http))
            print(f"[ALERTA] Caminho encontrado: {diretorio} - Status: {codigo_http}")
            registrar_log(f"Alvo {url_alvo} - Diretório {diretorio} retornou código {codigo_http}", "WARNING")
        else:
            print(f"[OK] {diretorio} - Nenhum dado exposto.")
            
    print("\n[*] Varredura finalizada.")
    registrar_log(f"Fim da varredura no alvo {url_alvo}", "INFO")
    return resultados

if __name__ == "__main__":
    escanear_alvo("google.com")

