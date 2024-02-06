import random

class ApiBatalha:
    def obterDadosAtaque(self, quantidade_exercitos_atacante):
        return self._simularLancamentoDados(min(quantidade_exercitos_atacante, 3))

    def obterDadosDefesa(self, quantidade_exercitos_defensor):
        return self._simularLancamentoDados(min(quantidade_exercitos_defensor, 2))

    def _simularLancamentoDados(self, quantidade):
        # Simula o lançamento de dados
        return [random.randint(1, 6) for _ in range(quantidade)]
