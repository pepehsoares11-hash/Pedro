# Sistema de Comissões de Vendedores

Aplicação didática com 3 endpoints, testes automatizados, Dockerfile e pipeline GitHub Actions. Usa Python e Flask.

**Escopo:** calcula a comissão de vendedores a partir do valor pago pelos clientes (percentual × total pago). Os dados são fictícios e ficam em memória, sendo perdidos ao reiniciar. Não tem banco de dados, autenticação nem importação de planilhas.

## Endpoints

- GET /vendedores
- GET /clientes
- GET /comissao/{id}

## Como rodar

```
docker run -p 5000:5000 pedrohsoares11/comissoes:latest
```

Ou, a partir do código:

```
docker build -t comissoes .
docker run -p 5000:5000 comissoes
```

## Testes

Testes automatizados de API com pytest (status das respostas, cálculo da comissão e erro 404 para vendedor inexistente):

```
python -m pytest
```

## Pipeline

A cada push, o GitHub Actions instala as dependências, roda os testes e, se passarem, constrói a imagem e publica no Docker Hub (`pedrohsoares11/comissoes`).