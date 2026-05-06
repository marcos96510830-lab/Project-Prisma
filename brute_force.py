import itertools

def testar_combinacoes():
    # A nossa senha secreta de teste
    senha_secreta = "1234"
    
    print("Testando combinações para decifrar a senha...")
    
    # Testando números de 1 a 4 dígitos
    for tamanho in range(1, 5):
        for tentativa in itertools.product("0123456789", repeat=tamanho):
            palavra = "".join(tentativa)
            if palavra == senha_secreta:
                print(f"\n[SUCESSO] A senha secreta é: {palavra}")
                return
    print("\n[FALHA] Combinação não encontrada.")

testar_combinacoes()

