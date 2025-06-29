# FastAPI Codes

Este repositório contém exemplos práticos de uso do [FastAPI](https://fastapi.tiangolo.com/), incluindo operações básicas de GET e POST.

## Estrutura dos Diretórios

- `01_simple_get_post/`  
  Exemplo simples de API com FastAPI, incluindo operações GET e POST.

## Como Executar o Exemplo

1. Acesse o diretório do exemplo:
   ```sh
   cd 01_simple_get_post```
2. Instale as dependências

``` pip install fastapi uvicorn httpx ```

3. Inicie o servidor FastAPI:

```uvicorn main:app --reload```

4. Teste a API utilizando o script de requisição:

```python httpx/request_https.py```

Endpoints do Exemplo
- GET /
Lista todos os itens cadastrados.

- POST /itens/
Cria um novo item. Exemplo de payload:

```
{
  "nome": "Caderno",
  "preco": 15.5,
  "disponivel": true
}
```

Observações
- Os dados são armazenados apenas em memória (não persistem após reiniciar o servidor).
- A documentação interativa da API estará disponível em http://127.0.0.1:8000/docs.