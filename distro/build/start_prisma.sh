#!/bin/bash
# Script de Inicialização da Distro Prisma

# 1. Mostra o banner antes de entrar
python3 ~/Project-Prisma/distro/core/identity.py

# 2. Faz o login no Alpine
echo -e "\n\033[1;32m[+]\033[0m Entrando no ambiente seguro..."
proot-distro login alpine

