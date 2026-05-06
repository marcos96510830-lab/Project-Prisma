class LunesEthicsEngine:
    def __init__(self):
        # Regras éticas fundamentais
        self.regras_autorizadas = ["auditoria", "defesa", "ethical_hacking"]
        self.limiar_risco = 5  # Escala de 1 a 10 para o nível de intrusão

    def verificar_acao(self, acao_proposta, nivel_risco):
        if nivel_risco > self.limiar_risco:
            print(f"[BLOQUEADO] Ação: '{acao_proposta}' excede o limite ético de risco.")
            return False
        
        if acao_proposta not in self.regras_autorizadas:
            print(f"[BLOQUEADO] Ação: '{acao_proposta}' não está na lista de operações éticas.")
            return False

        print(f"[PERMITIDO] Ação: '{acao_proposta}' aprovada pelas diretrizes éticas.")
        return True

# Exemplo de teste da nossa Engine
lunes = LunesEthicsEngine()
lunes.verificar_acao("ethical_hacking", nivel_risco=3)

