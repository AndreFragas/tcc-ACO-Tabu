from typing import List
from random import shuffle
from classes.ponto import Ponto

def distribuir_pontos_entre_motoboys(pontos: List[Ponto], quantidade_motoboys: int) -> List[List[Ponto]]:
    pontos_sem_A = [ponto for ponto in pontos if ponto.nome != "A"]
    pontos_por_motoboy = [[] for _ in range(quantidade_motoboys)]
    shuffle(pontos_sem_A)

    for i, ponto in enumerate(pontos_sem_A):
        pontos_por_motoboy[i % quantidade_motoboys].append(ponto)

    for i in range(quantidade_motoboys):
        pontos_por_motoboy[i].insert(0, pontos[0])

    return pontos_por_motoboy
