from typing import List
from classes.formiga import Formiga
from classes.ponto import Ponto
from classes.tabela_probabilidades import TabelaDeProbabilidades

def executar_aco(pontos: List[Ponto], tabela_de_probabilidades: List[TabelaDeProbabilidades], num_iteracoes: int):
    melhor_solucao = None
    melhor_distancia = float('inf')

    for _ in range(num_iteracoes):
        formigas = [Formiga(pontos, tabela_de_probabilidades) for _ in range(len(pontos))]
        
        for formiga in formigas:
            formiga.percorrer()
            
            if formiga.distancia_total < melhor_distancia:
                melhor_solucao = formiga.caminho  
                melhor_distancia = formiga.distancia_total

            for tabela in formiga.feromonios_depositados:
                tabela.atualizarFeromonio(1 / formiga.distancia_total)  
        
        for tabela in tabela_de_probabilidades:
            tabela.atualizarFeromonio(0)  

    return melhor_solucao, melhor_distancia