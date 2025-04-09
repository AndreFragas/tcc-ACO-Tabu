import random
from copy import deepcopy
from typing import List

from classes.ponto import Ponto

def trocar_rotas(pontos_por_motoboy: List[List[Ponto]]) -> List[List[Ponto]]:
    nova_distribuicao = deepcopy(pontos_por_motoboy)

    for i in range(len(nova_distribuicao)):
        pontos_i = nova_distribuicao[i]
        pontos_sem_a_i = [p for p in pontos_i if p.nome != "A"]

        if not pontos_sem_a_i:
            continue

        ponto_troca_i = random.choice(pontos_sem_a_i)

        # Encontrar outro motoboy para trocar
        j = i
        while j == i or not any(p.nome != "A" for p in nova_distribuicao[j]):
            j = random.randint(0, len(nova_distribuicao) - 1)

        pontos_j = nova_distribuicao[j]
        pontos_sem_a_j = [p for p in pontos_j if p.nome != "A"]
        ponto_troca_j = random.choice(pontos_sem_a_j)

        # Realiza a troca
        idx_i = nova_distribuicao[i].index(ponto_troca_i)
        idx_j = nova_distribuicao[j].index(ponto_troca_j)
        nova_distribuicao[i][idx_i], nova_distribuicao[j][idx_j] = ponto_troca_j, ponto_troca_i

    return nova_distribuicao
