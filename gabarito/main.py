from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# ===============
# LIGHTHOUSE 2026
# ===============

# EXERCÍCIO PRÁTICO: Tente refazer a api apresentada em aula. 
# Em caso de dúvida consulte a documentação em: https://fastapi.tiangolo.com/tutorial/ 


# Criação da aplicação FastAPI

# Dicionário simulando um banco de dados em memória
# Cada item possui um id, nome e descrição
# Inicialmente, temos dois itens cadastrados


# Modelo de dados para entrada e saída de itens


# Rota GET para listar todos os itens cadastrados
# Exemplo de uso: GET /items


# Rota GET para buscar um item específico pelo ID
# Exemplo de uso: GET /items/1


# Rota POST para criar um novo item
# Exemplo de uso: POST /items com body {"name": "Item 3", "description": "Terceiro item"}


# Rota PUT para atualizar um item existente
# Exemplo de uso: PUT /items/1 com body {"name": "Novo nome", "description": "Nova descrição"}


# Rota DELETE para remover um item
# Exemplo de uso: DELETE /items/1

