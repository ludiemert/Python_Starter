from flask import Flask, jsonify, request # Framework para criar APIs
from flask_cors import CORS # Permite que o frontend faça requisições à API, CORS é essencial em aplicações web para evitar bloqueios de requisições por domínios diferentes.
from datetime import datetime

app = Flask(__name__)
CORS(app)

carros = [
    {"id": 0, "nome": "Chevrolet Tracker", "preco": 120},
    {"id": 1, "nome": "Chevrolet Onix", "preco": 90},
    {"id": 2, "nome": "Chevrolet Spin", "preco": 150},
    {"id": 3, "nome": "Hyundai HB20", "preco": 85},
    {"id": 4, "nome": "Hyundai Tucson", "preco": 120},
    {"id": 5, "nome": "Fiat Uno", "preco": 60}
]

alugados = [] #será preenchido ao longo do uso.
#Simula um banco de dados simples em memória.


# Rotas da API

# Listar carros, Retorna os dados de carros disponíveis e alugados.
@app.route('/api/carros', methods=['GET'])
def listar_carros():
    return jsonify({"carros": carros, "alugados": alugados})

# Alugar carro, Calcula o preço total baseado nos dias.
# Remove o carro da lista de disponíveis e o adiciona na de alugados. Atualiza dinamicamente os estados no backend.
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

    return jsonify({'message': 'Car successfully rented!'})

# Devolver carro
@app.route('/api/devolver', methods=['POST'])
def devolver_carro(): # Remove o carro de "alugados" e o adiciona em "carros".
    data = request.json
    carro_id = data.get("id")

    for carro in alugados:
        if carro["id"] == carro_id:
            alugados.remove(carro)
            carros.append(carro) # # Remove o carro de "alugados" e o adiciona em "carros".
            return jsonify({"message": "Car successfully returned!"}), 200

    return jsonify({"message": "Car not found!"}), 404

#Roda o servidor localmente.
# Modo debug facilita encontrar erros durante o desenvolvimento.
if __name__ == '__main__':
    app.run(debug=True)
