from typing import List
from classes.ponto import Ponto

def rebalancear_porcentagens(lista: List[Ponto]) -> None:
    soma_porcentagens = sum(item.porcentagem for item in lista)
    if soma_porcentagens == 0:
        return
    
    for item in lista: 
        item.porcentagem = (item.porcentagem / soma_porcentagens) * 100