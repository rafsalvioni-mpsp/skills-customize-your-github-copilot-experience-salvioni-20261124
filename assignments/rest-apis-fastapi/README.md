# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Criar uma API REST em Python com o framework FastAPI, implementando rotas de leitura, criação, atualização e remoção de recursos, com validação de dados usando Pydantic.

## 📝 Tarefas

### 🛠️ Criar rotas de leitura

#### Descrição
Instale o FastAPI e o Uvicorn (`pip install fastapi uvicorn`), salve o [starter code](starter-code.py) como `main.py` e execute com `uvicorn main:app --reload`. Depois, crie as rotas que listam e consultam os itens armazenados em memória.

#### Requisitos
O programa concluído deve:

- Responder `GET /items` com a lista de todos os itens
- Responder `GET /items/{item_id}` com o item correspondente
- Retornar status 404 quando o item não existir


### 🛠️ Validar dados com Pydantic

#### Descrição
Crie um modelo Pydantic para representar um item e use-o na rota de criação.

#### Requisitos
O programa concluído deve:

- Definir o modelo `Item` com os campos `name` (texto), `price` (número maior que zero) e `quantity` (inteiro não negativo)
- Responder `POST /items` com status 201 e o item criado, incluindo um `id` gerado automaticamente
- Retornar erro 422 quando os dados enviados forem inválidos


### 🛠️ Atualizar e remover itens

#### Descrição
Complete o CRUD da API implementando as rotas de atualização e remoção, e teste todas as rotas pela documentação interativa em `/docs`.

#### Requisitos
O programa concluído deve:

- Responder `PUT /items/{item_id}` substituindo os dados do item e retornando o item atualizado
- Responder `DELETE /items/{item_id}` com status 204 após remover o item
- Retornar status 404 nas rotas de atualização e remoção quando o item não existir
