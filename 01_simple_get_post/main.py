from fastapi import FastAPI
from models import Item

app = FastAPI()

# Simula um "banco de dados" em memória
itens_db = []

@app.get("/")
def listar_itens():
    return {"itens": itens_db}

@app.post("/itens/")
def criar_item(item: Item):
    itens_db.append(item)
    return {"mensagem": "Item criado com sucesso!", "item": item}
