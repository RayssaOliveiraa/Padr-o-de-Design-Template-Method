# EstrategiaBatalhaAgressiva.py
from EstrategiaBatalha import EstrategiaBatalha

class EstrategiaBatalhaAgressiva(EstrategiaBatalha):
    def calcularQuantidadeDadosAtaque(self, quantidade_exercitos):
        if quantidade_exercitos >= 3:
            return self.api.obterDadosAtaque(3)
        elif quantidade_exercitos == 2:
            return self.api.obterDadosAtaque(2)
        elif quantidade_exercitos == 1:
            return self.api.obterDadosAtaque(1)
        else:
            return self.api.obterDadosAtaque(0)

    def calcularQuantidadeDadosDefesa(self, quantidade_exercitos):
        return self.api.obterDadosDefesa(quantidade_exercitos)

    def realizarBatalha(self, ataque, defesa):
        return f"Batalha Agressiva realizada - Ataque: {ataque}"

    def obterDetalhes(self):
        return "Estrategia Agressiva - Dados lancados de acordo com a quantidade de exercitos."