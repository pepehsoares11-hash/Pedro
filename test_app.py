from app import app

def test_vendedores():
    cliente = app.test_client()
    resposta = cliente.get("/vendedores")
    assert resposta.status_code == 200
    assert len(resposta.get_json()) == 2

def test_clientes():
    cliente = app.test_client()
    resposta = cliente.get("/clientes")
    assert resposta.status_code == 200
    assert len(resposta.get_json()) == 3

def test_comissao_ana():
    cliente = app.test_client()
    resposta = cliente.get("/comissao/1")
    assert resposta.status_code == 200
    assert resposta.get_json()["comissao"] == 75.0

def test_vendedor_inexistente():
    cliente = app.test_client()
    resposta = cliente.get("/comissao/99")
    assert resposta.status_code == 404