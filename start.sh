#!/usr/bin/env bash
set -e

# Garante que estamos na pasta do script
cd "$(dirname "$0")"

# Verifica se o ambiente virtual existe, senão cria
if [ ! -d ".venv" ]; then
    echo "Criando o ambiente virtual (.venv)..."
    python3 -m venv .venv
fi

# Ativa o ambiente virtual
echo "Ativando o ambiente virtual..."
source .venv/bin/activate

# Instala as dependências se o requirements.txt existir
if [ -f "requirements.txt" ]; then
    echo "Verificando e instalando dependências..."
    pip install --upgrade pip > /dev/null
    pip install -r requirements.txt > /dev/null
fi

# Executa o script principal de separação de camadas
echo "Executando o processador de imagem..."
python3 script.py "Screenshot from 2026-11-01 08-22-14.png"

echo "Processo concluído com sucesso!"

