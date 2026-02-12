#!/bin/bash

echo "--- Iniciando o Build ---"

# Instala as dependências (caso não seja feito automaticamente)
pip install -r requirements.txt

# Roda as Migrations
echo "--- Rodando Migrations ---"
#python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Coleta os arquivos estáticos (WhiteNoise)
echo "--- Coletando Static Files ---"
python3 manage.py collectstatic --noinput

echo "--- Build Finalizado ---"