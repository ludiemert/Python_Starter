from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

carros = [
    {"id": 0, "nome": "Chevrolet Tracker", "preco": 120},
    {"id": 1, "nome": "Chevrolet Onix", "preco": 90},
    {"id": 2, "nome": "Chevrolet Spin", "preco": 150},
    {"id": 3, "nome": "Hyundai HB20", "preco": 85},
    {"id": 4, "nome": "Hyundai Tucson", "preco": 120},
    {"id": 5, "nome": "Fiat Uno", "preco": 60},
    {"id": 6, "nome": "Fiat Mobi", "preco": 100},
    {"id": 7, "nome": "Fiat Pulse", "preco": 130}
]

alugados = []

@app.route('/api/carros', methods=['GET'])
def listar_carros():
    return jsonify({"carros": carros, "alugados": alugados})

@app.route('/api/alugar', methods=['POST'])
def alugar_carro():
    data = request.json
    carro_id = data['id']
    data_retirada = data['data_retirada']
    data_entrega = data['data_entrega']

    # Calculando dias e preço
    data_inicio = datetime.strptime(data_retirada, '%Y-%m-%d')
    data_fim = datetime.strptime(data_entrega, '%Y-%m-%d')
    diff_days = (data_fim - data_inicio).days
    carro = next(c for c in carros if c['id'] == carro_id)
    total_preco = carro['preco'] * diff_days

    # Atualizando o carro alugado
    carro['disponivel'] = False
    carro['data_retirada'] = data_retirada
    carro['data_entrega'] = data_entrega
    carro['dias'] = diff_days
    carro['total_preco'] = total_preco

    # Movendo o carro para a lista de alugados
    alugados.append(carro)
    carros.remove(carro)

    return jsonify({'message': 'Carro alugado com sucesso!'})

@app.route('/api/devolver', methods=['POST'])
def devolver_carro():
    data = request.json
    carro_id = data.get("id")

    for carro in alugados:
        if carro["id"] == carro_id:
            alugados.remove(carro)
            carros.append(carro)
            return jsonify({"message": "Carro devolvido com sucesso!"}), 200

    return jsonify({"message": "Carro não encontrado!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
