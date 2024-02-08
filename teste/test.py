# tests/testes.py
import unittest
from unittest.mock import patch
from ApiBatalha import ApiBatalha
from EstrategiaBatalhaAgressiva import EstrategiaBatalhaAgressiva
from EstrategiaBatalhaDefensiva import EstrategiaBatalhaDefensiva

class TestApiBatalha(unittest.TestCase):

    def setUp(self):
        self.api_batalha = ApiBatalha()

    def test_obter_dados_ataque(self):
        quantidade_exercitos_atacante = 3

        with patch.object(ApiBatalha, '_simularLancamentoDados', return_value=[4, 5, 6]):
            resultado = self.api_batalha.obterDadosAtaque(quantidade_exercitos_atacante)

        self.assertEqual(resultado, [4, 5, 6])

    def test_obter_dados_defesa(self):
        quantidade_exercitos_defensor = 2

        with patch.object(ApiBatalha, '_simularLancamentoDados', return_value=[2, 3]):
            resultado = self.api_batalha.obterDadosDefesa(quantidade_exercitos_defensor)

        self.assertEqual(resultado, [2, 3])

    def test_logica_jogo(self):
        # Criar instâncias de estratégias e API
        estrategia_agressiva = EstrategiaBatalhaAgressiva(self.api_batalha)
        estrategia_defensiva = EstrategiaBatalhaDefensiva(self.api_batalha)

        # Configurar quantidade de exércitos para o teste
        quantidade_exercitos_agressiva = 3
        quantidade_exercitos_defensiva = 2

        # Simular dados de ataque e defesa
        dados_ataque_agressiva = [4, 5, 6]
        dados_ataque_defensiva = [4, 5]
        dados_defesa = [2, 3]

        # Criar patch para simular a geração de dados
        with patch.object(ApiBatalha, '_simularLancamentoDados') as mock_simular_lancamento:
            mock_simular_lancamento.side_effect = [dados_ataque_agressiva, dados_defesa, dados_ataque_defensiva, dados_defesa]

            # Executar batalhas
            resultado_agressiva = estrategia_agressiva.executeBatalha(quantidade_exercitos_agressiva)
            resultado_defensiva = estrategia_defensiva.executeBatalha(quantidade_exercitos_defensiva)

        # Verificar se os resultados estão corretos
        self.assertEqual(resultado_agressiva, "Batalha Agressiva realizada - Ataque: [4, 5, 6], Defesa: [2, 3]")
        self.assertEqual(resultado_defensiva, "Batalha Defensiva realizada - Ataque: [4, 5], Defesa: [2, 3]")

if __name__ == '__main__':
    unittest.main()
