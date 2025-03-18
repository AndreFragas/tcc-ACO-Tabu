from classes.ponto import Ponto
from geopy.distance import distance

def calcular_distancia(ponto1: Ponto, ponto2: Ponto) -> float:
    coordenada_1 = (ponto1.latitude, ponto1.longitude)
    coordenada_2 = (ponto2.latitude, ponto2.longitude)
    return distance(coordenada_1, coordenada_2).kilometers