# Sistema de Comissões de Vendedores

API simples (Flask) com 3 endpoints:

- GET /vendedores
- GET /clientes
- GET /comissao/<id>

## Como rodar

docker build -t comissoes .
docker run -p 5000:5000 comissoes