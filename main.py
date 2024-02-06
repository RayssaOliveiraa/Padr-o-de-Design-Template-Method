# main.py
from flask import Flask, jsonify
from ApiBatalha import ApiBatalha
from EstrategiaBatalhaAgressiva import EstrategiaBatalhaAgressiva
from EstrategiaBatalhaDefensiva import EstrategiaBatalhaDefensiva

app = Flask(__name__)

# Criando uma instância da classe ApiBatalha
api_batalha = ApiBatalha()

# Criando estratégias de batalha
estrategia_agressiva = EstrategiaBatalhaAgressiva(api_batalha)
estrategia_defensiva = EstrategiaBatalhaDefensiva(api_batalha)

@app.route('/batalha/agressiva/<valor>')
def batalha_agressiva(valor):
    resultado_agressivo = estrategia_agressiva.executeBatalha(int(valor))
    detalhes_agressivos = estrategia_agressiva.obterDetalhes()
    return jsonify({"resultado": resultado_agressivo, "detalhes": detalhes_agressivos})

@app.route('/batalha/defensiva/<valor>')
def batalha_defensiva(valor):
    resultado_defensivo = estrategia_defensiva.executeBatalha(int(valor))
    detalhes_defensivos = estrategia_defensiva.obterDetalhes()
    return jsonify({"resultado": resultado_defensivo, "detalhes": detalhes_defensivos})

if __name__ == '__main__':
    app.run(debug=True)