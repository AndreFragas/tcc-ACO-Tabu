from typing import List
from classes.ponto import Ponto
from funcoes.trocar_rotas import trocar_rotas
from funcoes.aco import executar_aco
from funcoes.calcular_probabilidades import calcular_probabilidades
from funcoes.criar_tabela_de_probabilidades import criar_tabela_de_probabilidades
from funcoes.distribuir_pontos_entre_motoboys import distribuir_pontos_entre_motoboys


def otimizar_com_trocas(
    pontos: List[Ponto],
    quantidade_motoboys: int,
    num_iteracoes_aco: int,
    feromonio_inicial: float,
    coef_evaporacao: float,
    max_tentativas_sem_melhora: int = 25,
    const_att_feromonios: float = 0,
):
    melhor_resultado = None
    menor_distancia_total = float('inf')
    tentativas_sem_melhora = 0

    # Primeira distribuição e execução
    pontos_por_motoboy = distribuir_pontos_entre_motoboys(pontos, quantidade_motoboys)

    iteracao = 0
    while tentativas_sem_melhora < max_tentativas_sem_melhora:
        iteracao += 1
        print(f"\nIteração de troca {iteracao}")

        if iteracao > 1:
            pontos_por_motoboy = trocar_rotas(pontos_por_motoboy)

        resultados = []
        for pontos_motoboy in pontos_por_motoboy:
            tabela_probabilidades = criar_tabela_de_probabilidades(pontos_motoboy, feromonio_inicial, coef_evaporacao)
            calcular_probabilidades(pontos_motoboy, tabela_probabilidades)
            resultado = executar_aco(pontos_motoboy, tabela_probabilidades, num_iteracoes_aco, const_att_feromonios)
            resultados.append(resultado)

        soma_total = sum(dist for _, dist in resultados)

        if soma_total < menor_distancia_total:
            menor_distancia_total = soma_total
            melhor_resultado = resultados
            tentativas_sem_melhora = 0
            print(f"✨ Novo melhor resultado com soma de distâncias: {menor_distancia_total}")
        else:
            tentativas_sem_melhora += 1
            print(f"Nenhuma melhoria. Tentativas sem melhoria: {tentativas_sem_melhora}")

    print(f"\nFinalizado após {iteracao} iterações. Melhor soma de distâncias: {menor_distancia_total}")
    return melhor_resultado
