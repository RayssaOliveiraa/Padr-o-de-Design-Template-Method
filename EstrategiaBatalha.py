# EstrategiaBatalha.py
from abc import ABC, abstractmethod

class EstrategiaBatalha(ABC):
    def __init__(self, api_batalha):
        self.api = api_batalha

    def executeBatalha(self, quantidade_exercitos):
        ataque = self.calcularQuantidadeDadosAtaque(quantidade_exercitos)
        defesa = self.calcularQuantidadeDadosDefesa(quantidade_exercitos)
        resultado = self.realizarBatalha(ataque, defesa)
        return resultado

    @abstractmethod
    def calcularQuantidadeDadosAtaque(self, quantidade_exercitos):
        pass

    @abstractmethod
    def calcularQuantidadeDadosDefesa(self, quantidade_exercitos):
        pass

    @abstractmethod
    def realizarBatalha(self, ataque, defesa):
        pass

    def formatarResultadoBatalha(self, ataque, defesa):
        return f"Batalha realizada com sucesso -Dados vermelho: Ataque: {ataque} , Dados Amarelos Defesa: {defesa}"
