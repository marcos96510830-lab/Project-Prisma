# Project Prisma 🛡️

O Project Prisma é uma arquitetura de segurança, auditoria e ethical hacking projetada para ambientes móveis (Termux) e infraestruturas conectadas.

## Módulos do Projeto

Todos os módulos estão organizados dentro da pasta `src/`:
* **src/prisma_check.py**: Raio-x do sistema, verificação de espaço em disco e integridade.
* **src/security_alert.py**: Sistema de auditoria e notificação de eventos críticos.
* **src/recuperar_senha.py**: Ferramenta de recuperação automatizada de chaves GPG.
* **src/lunes_etica.py**: Engine de diretrizes éticas que delimita a atuação do módulo Lunes.
* **src/lunes_update.py**: Agente do Lunes para verificação e atualização de pacotes (`pkg update/upgrade`).
* **src/run_prisma.py**: Automação central de inicialização do sistema e integração com o GitHub.

## Como Executar

Para iniciar todo o projeto, utilize o atalho configurado no terminal:
* prisma

## Contribuidores
​Marcos (Security Development)
