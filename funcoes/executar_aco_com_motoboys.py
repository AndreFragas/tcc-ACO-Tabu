from typing import List
from classes.ponto import Ponto
from classes.tabela_probabilidades import TabelaDeProbabilidades
from funcoes.distribuir_pontos_entre_motoboys import distribuir_pontos_entre_motoboys
from funcoes.aco import executar_aco
from funcoes.criar_tabela_de_probabilidades import criar_tabela_de_probabilidades
from funcoes.calcular_probabilidades import calcular_probabilidades

def executar_aco_com_motoboys(pontos: List[Ponto], quantidade_motoboys: int, num_iteracoes: int, feromonio_inicial: float, coeficiente_de_evaporacao: float):
    pontos_por_motoboy = distribuir_pontos_entre_motoboys(pontos, quantidade_motoboys)
    resultados_motoboys = []
    
    for i, pontos_motoboy in enumerate(pontos_por_motoboy):
        print(f"Executando ACO para o motoboy {i + 1} com os pontos: {[p.nome for p in pontos_motoboy]}")

        tabela_de_probabilidades_motoboy = criar_tabela_de_probabilidades(pontos_motoboy, feromonio_inicial, coeficiente_de_evaporacao) 

        calcular_probabilidades(pontos_motoboy, tabela_de_probabilidades_motoboy)
        
        resultado_motoboy = executar_aco(pontos_motoboy, tabela_de_probabilidades_motoboy, num_iteracoes)
        resultados_motoboys.append(resultado_motoboy)
    
    return resultados_motoboys

