from flask import Flask, jsonify

app = Flask(__name__)

vendedores = [
    {"id": 1, "nome": "Ana", "percentual": 0.05},
    {"id": 2, "nome": "Bruno", "percentual": 0.08},
]

clientes = [
    {"id": 1, "nome": "Cliente A", "vendedor_id": 1, "valor_pago": 1000},
    {"id": 2, "nome": "Cliente B", "vendedor_id": 1, "valor_pago": 500},
    {"id": 3, "nome": "Cliente C", "vendedor_id": 2, "valor_pago": 2000},
]

@app.route("/vendedores")
def listar_vendedores():
    return jsonify(vendedores)

@app.route("/clientes")
def listar_clientes():
    return jsonify(clientes)

@app.route("/comissao/<int:vendedor_id>")
def comissao(vendedor_id):
    vendedor = next((v for v in vendedores if v["id"] == vendedor_id), None)
    if vendedor is None:
        return jsonify({"erro": "Vendedor não encontrado"}), 404

    total = sum(c["valor_pago"] for c in clientes if c["vendedor_id"] == vendedor_id)
    return jsonify({
        "vendedor": vendedor["nome"],
        "total_pago_pelos_clientes": total,
        "percentual": vendedor["percentual"],
        "comissao": total * vendedor["percentual"],
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)