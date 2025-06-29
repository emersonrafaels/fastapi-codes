import httpx

# URL da sua API local
BASE_URL = "http://127.0.0.1:8000"

def listar_itens():
    response = httpx.get(f"{BASE_URL}/")
    print(response.status_code)
    print(response.json())

def criar_item():
    novo_item = {
        "nome": "Caderno",
        "preco": 15.5,
        "disponivel": True
    }
    response = httpx.post(f"{BASE_URL}/itens/", json=novo_item)
    print(response.status_code)
    print(response.json())

# Executando
listar_itens()
criar_item()
listar_itens()
