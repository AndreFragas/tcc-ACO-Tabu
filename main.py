from typing import List
from classes.ponto import Ponto
from funcoes.criar_tabela_de_probabilidades import criar_tabela_de_probabilidades
from funcoes.calcular_probabilidades import calcular_probabilidades
from funcoes.aco import executar_aco

pontos: List[Ponto] = [
    Ponto("A", -26.3807755, -48.8279418),
    Ponto("B", -26.3686852, -48.828794),
    Ponto("C", -26.3689887, -48.848882),
    Ponto("D", -26.3686007, -48.8231558),
    Ponto("E", -26.3686252, -48.8245343),
]
quantidade_formigas = len(pontos)
quantidade_motoboys = 3
alfa = 1
beta = 1
coeficiente_de_evaporacao = 0.01
feromonio_inicial = 0.1
constante_de_atualizacao_do_feromonio = 10
iteracoes_aco = 5
iteracoes_tabu = 5
tabela_de_probabilidades = criar_tabela_de_probabilidades(pontos, feromonio_inicial, coeficiente_de_evaporacao)

calcular_probabilidades(pontos, tabela_de_probabilidades)

resultado = executar_aco(pontos, tabela_de_probabilidades, iteracoes_aco)
print(resultado)