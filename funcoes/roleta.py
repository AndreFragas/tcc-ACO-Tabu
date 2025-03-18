import random
from typing import List
from classes.ponto import Ponto

def roleta(lista: List[Ponto]) -> Ponto:
    pesos = [item.porcentagem for item in lista]
    sorteado = random.choices(lista, weights=pesos, k=1)
    return sorteado[0]

