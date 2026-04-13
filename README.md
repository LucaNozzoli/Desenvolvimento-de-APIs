# Desenvolvimento-de-APIs

Este projeto apresenta um exemplo prático e didático de construção de APIs RESTful utilizando o framework FastAPI em Python. O objetivo é servir como base para aulas práticas, demonstrando conceitos fundamentais como rotas, métodos HTTP, códigos de status, manipulação de dados e tratamento de erros.

## Como executar a API localmente

### 1. Crie e ative um ambiente virtual (recomendado)

```bash
python3 -m venv desenvolvimento_apis
source desenvolvimento_apis/bin/activate
```

### 2. Instale as dependências do projeto
```bash
pip install -r requirements.txt
```

### 3. Execute o servidor localmente:

```bash
uvicorn main:app --reload
```

- O parâmetro `--reload` faz com que o servidor reinicie automaticamente ao salvar alterações no código.
- A API estará disponível em: http://127.0.0.1:8000
- A documentação interativa estará em: http://127.0.0.1:8000/docs

## Exemplos de requisições

### Listar todos os itens (GET)
```
GET /items
```

### Buscar item por ID (GET)
```
GET /items/1
```

### Criar novo item (POST)
```
POST /items
Body: { "name": "Item 3", "description": "Terceiro item" }
```

### Atualizar item (PUT)
```
PUT /items/1
Body: { "name": "Novo nome", "description": "Nova descrição" }
```

### Remover item (DELETE)
```
DELETE /items/1
```

## Como testar a API

Você pode testar a API de três formas:

1. Usando a documentação interativa do FastAPI em http://127.0.0.1:8000/docs
2. Utilizando ferramentas como [Insomnia](https://insomnia.rest/) ou [Postman](https://www.postman.com/)
3. Usando o comando `curl` no terminal. Exemplo:

```bash
curl -X GET http://127.0.0.1:8000/items
```

---

Este projeto serve como base didática para aulas práticas de desenvolvimento de APIs com FastAPI.