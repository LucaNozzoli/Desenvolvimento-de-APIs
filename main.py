from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Criação da aplicação FastAPI
app = FastAPI()

# Dicionário simulando um banco de dados em memória
# Cada item possui um id, nome e descrição
# Inicialmente, temos dois itens cadastrados
items_db = {
    1: {"name": "Item 1", "description": "Primeiro item"},
    2: {"name": "Item 2", "description": "Segundo item"}
}

# Modelo de dados para entrada e saída de itens
class Item(BaseModel):
    name: str
    description: Optional[str] = None

# Rota GET para listar todos os itens cadastrados
# Exemplo de uso: GET /items
@app.get("/items", status_code=200)
def list_items():
    """Retorna todos os itens cadastrados."""
    return items_db

# Rota GET para buscar um item específico pelo ID
# Exemplo de uso: GET /items/1
@app.get("/items/{item_id}", status_code=200)
def get_item(item_id: int):
    """Retorna um item pelo seu ID. Se não existir, retorna erro 404."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return items_db[item_id]

# Rota POST para criar um novo item
# Exemplo de uso: POST /items com body {"name": "Item 3", "description": "Terceiro item"}
@app.post("/items", status_code=201)
def create_item(item: Item):
    """Cria um novo item. Retorna o item criado com seu novo ID."""
    new_id = max(items_db.keys(), default=0) + 1
    items_db[new_id] = item.dict()
    return {"id": new_id, **item.dict()}

# Rota PUT para atualizar um item existente
# Exemplo de uso: PUT /items/1 com body {"name": "Novo nome", "description": "Nova descrição"}
@app.put("/items/{item_id}", status_code=200)
def update_item(item_id: int, item: Item):
    """Atualiza um item existente. Se não existir, retorna erro 404."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    items_db[item_id] = item.dict()
    return {"id": item_id, **item.dict()}

# Rota DELETE para remover um item
# Exemplo de uso: DELETE /items/1
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Remove um item pelo ID. Se não existir, retorna erro 404."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del items_db[item_id]
    return None
