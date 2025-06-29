from pydantic import BaseModel

class Item(BaseModel):
    nome: str
    preco: float
    disponivel: bool = True
