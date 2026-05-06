import subprocess

def testar_senha_gpg(caminho_arquivo, senha):
    try:
        comando = f"gpg --pinentry-mode loopback --batch --passphrase '{senha}' -d {caminho_arquivo}"
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        
        if resultado.returncode == 0:
            print(f"\n[SUCESSO] A senha correta é: {senha}")
            return True
        else:
            return False
    except Exception as e:
        return False

# Variações da senha que estamos testando
tentativas = ["deuteronomio", "Deuteronomio", "deuteronômio", "Deuteronômio"]

arquivo_alvo = "~/Project-Prisma/dados_secretos.txt.gpg"

print("Iniciando varredura de recuperação com a variação informada...")
for senha in tentativas:
    if testar_senha_gpg(arquivo_alvo, senha):
        break
else:
    print("\n[FALHA] Nenhuma das variações testadas funcionou.")

