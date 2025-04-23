import random
from typing import List, Tuple, Dict
from classes.ponto import Ponto

def trocar_rotas_tabu(
    rotas: List[List[Ponto]],
    lista_tabu: Dict[str, int]
) -> Tuple[List[List[Ponto]], List[str]]:
    novas_rotas = [rota.copy() for rota in rotas]
    pontos_bloqueados = []

    for _ in range(10):  # tenta até 10 trocas possíveis
        m1, m2 = random.sample(range(len(novas_rotas)), 2)
        if len(novas_rotas[m1]) <= 1 or len(novas_rotas[m2]) <= 1:
            continue

        p1 = random.choice(novas_rotas[m1][1:])
        p2 = random.choice(novas_rotas[m2][1:])

        if p1.nome in lista_tabu or p2.nome in lista_tabu:
            continue

        i1 = novas_rotas[m1].index(p1)
        i2 = novas_rotas[m2].index(p2)

        novas_rotas[m1][i1], novas_rotas[m2][i2] = p2, p1
        pontos_bloqueados.extend([p1.nome, p2.nome])
        break

    return novas_rotas, pontos_bloqueados
