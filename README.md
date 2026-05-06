# Project Prisma 🛡️

O Project Prisma é uma arquitetura de segurança, auditoria e ethical hacking projetada para ambientes móveis (Termux) e infraestruturas conectadas.

## Módulos do Projeto

* **src/prisma_check.py**: Raio-x do sistema, verificação de espaço em disco e integridade dos arquivos de log.
* **src/security_alert.py**: Sistema de auditoria e notificação de eventos críticos e extração de dados.
* **src/recuperar_senha.py**: Ferramenta de recuperação automatizada de chaves GPG.
* **src/lunes_etica.py**: Engine de diretrizes éticas que delimita a atuação do módulo Lunes.

## Configuração e Instalação

Clone o repositório e instale os diretórios de log:
```bash
git clone [https://github.com/marcos96510830/Project-Prisma.git](https://github.com/marcos96510830/Project-Prisma.git)
cd Project-Prisma
python3 src/prisma_check.py

