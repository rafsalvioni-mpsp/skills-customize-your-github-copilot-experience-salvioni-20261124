from fastapi import FastAPI

app = FastAPI(title="API de Itens")

# Lista em memória usada como armazenamento
items: list[dict] = []


@app.get("/")
def read_root():
    return {"mensagem": "API de itens no ar"}


# TODO: definir o modelo Pydantic Item
# TODO: implementar as rotas de leitura, criação, atualização e remoção
