from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Permite CORS para todas as origens
CORS(app)

@app.route('/api/carros')
def carros():
    carros_data = [
        {"id": 0, "nome": "Chevrolet Tracker", "preco": 120},
        {"id": 1, "nome": "Chevrolet Onix", "preco": 90},
        {"id": 2, "nome": "Chevrolet Spin", "preco": 150},
        {"id": 3, "nome": "Hyundai HB20", "preco": 85},
        {"id": 4, "nome": "Hyundai Tucson", "preco": 120},
        {"id": 5, "nome": "Fiat Uno", "preco": 60},
        {"id": 6, "nome": "Fiat Mobi", "preco": 100},
        {"id": 7, "nome": "Fiat Pulse", "preco": 130}
    ]
    return jsonify({"carros": carros_data})

if __name__ == '__main__':
    app.run(debug=True)
