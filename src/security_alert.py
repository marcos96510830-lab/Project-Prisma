import os
import datetime

def registrar_evento(mensagem):
    # Obtém o diretório home do usuário atual
    home_dir = os.path.expanduser("~")
    log_dir = os.path.join(home_dir, "Project-Prisma")
    
    # Cria o diretório Project-Prisma se não existir
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file = os.path.join(log_dir, "seguranca.log")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_linha = f"[{timestamp}] ALERTA DE SEGURANÇA: {mensagem}\n"
    
    with open(log_file, "a") as f:
        f.write(log_linha)
    
    print(f"Registro salvo em: {log_file}")

# Registrando a operação confirmada
registrar_evento("Extração de dados concluída utilizando a chave: deuteronomio")

