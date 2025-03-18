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
            formiga.percorrer()  # A formiga percorre o caminho
            
            # Atualizar o melhor caminho encontrado
            if formiga.distancia_total < melhor_distancia:
                melhor_solucao = formiga.caminho
                melhor_distancia = formiga.distancia_total

            # Atualizar feromônio nas rotas percorridas pela formiga
            for tabela in formiga.feromonios_depositados:
                tabela.atualizarFeromonio(1 / formiga.distancia_total)  # delta de feromônio baseado na distância
        
        # Evaporar feromônio após todas as formigas passarem
        for tabela in tabela_de_probabilidades:
            tabela.atualizarFeromonio(0)  # Aplicar coeficiente de evaporação de feromônio

    melhor_solucao_str = " ".join(melhor_solucao)
    return melhor_solucao_str, melhor_distancia