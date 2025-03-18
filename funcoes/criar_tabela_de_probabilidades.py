from classes.ponto import Ponto
from classes.tabela_probabilidades import TabelaDeProbabilidades
from funcoes.calcular_distancia import calcular_distancia

def criar_tabela_de_probabilidades(pontos: list[Ponto], feromonio_inicial: float, coeficiente_de_evaporacao: float) -> list[TabelaDeProbabilidades]:
    tabela_de_probabilidades: list[TabelaDeProbabilidades] = []
    for i, ponto_origem in enumerate(pontos):
        for j, ponto_destino in enumerate(pontos):
            if i != j:
                distancia = calcular_distancia(ponto_origem, ponto_destino)
                tabela_probabilidade = TabelaDeProbabilidades(
                    rota=f"{ponto_origem.nome} -> {ponto_destino.nome}",
                    distancia=distancia,
                    feromonio_inicial=feromonio_inicial,
                    coeficiente_de_evaporacao=coeficiente_de_evaporacao
                )
                tabela_de_probabilidades.append(tabela_probabilidade)
    return tabela_de_probabilidades