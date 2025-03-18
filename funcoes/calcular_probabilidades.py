from classes.ponto import Ponto
from classes.tabela_probabilidades import TabelaDeProbabilidades

def calcular_probabilidades(pontos: list[Ponto], tabela_de_probabilidades: list[TabelaDeProbabilidades]) -> None:
    for ponto_origem in pontos:
        relacoes = [tabela.relacao for tabela in tabela_de_probabilidades if tabela.rota.startswith(f"{ponto_origem.nome} ->")]
        
        for tabela in tabela_de_probabilidades:
            if tabela.rota.startswith(f"{ponto_origem.nome} ->"):
                tabela.calcularProbabilidade(relacoes)