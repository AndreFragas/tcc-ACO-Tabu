import time
from typing import List
from classes.ponto import Ponto
from funcoes.otimizar_com_trocas import otimizar_com_trocas

pontos: List[Ponto] = [
    Ponto("A", -26.3807755, -48.8279418),
    Ponto("B", -26.3686852, -48.828794),
    Ponto("C", -26.3689887, -48.848882),
    Ponto("D", -26.3686007, -48.8231558),
    Ponto("E", -26.3686252, -48.8245343),
    Ponto("F", -26.342658, -48.8330551),
    Ponto("G", -26.2807694, -48.856656),
    Ponto("H", -26.2930272, -48.8565296),
    Ponto("I", -26.3685505, -48.8226621),
    Ponto("J", -26.2477244, -48.8173741),
    Ponto("K", -26.2181748, -48.7997026),
    Ponto("L", -26.2815263, -48.8729415),
    Ponto("M", -26.2168325, -48.8129301),
    Ponto("N", -26.3130198, -48.856833),
    Ponto("O", -26.3247362, -48.7980792),
    Ponto("P", -26.3527274, -48.8303964),
    Ponto("Q", -26.3376999, -48.8712602),
    Ponto("R", -26.3666465, -48.8367379),
    Ponto("S", -26.3685995, -48.8202019),
    Ponto("T", -26.3187833, -48.8540092),
    Ponto("U", -26.2942143, -48.852169),
    Ponto("V", -26.3302516, -48.8484033),
    Ponto("W", -26.2601708, -48.8144716),
    Ponto("X", -26.2835841, -48.8535669),
    Ponto("Y", -26.3284629, -48.7958883),
    Ponto("Z", -26.3360418, -48.8477327),
]
quantidade_motoboys = 5
iteracoes_aco = 1000
feromonio_inicial = 0.1
coeficiente_de_evaporacao = 0.01
max_tentativas_sem_melhora = 100
const_att_feromonios = 10

inicio = time.time()

melhor_resultado = otimizar_com_trocas(
    pontos,
    quantidade_motoboys,
    iteracoes_aco,
    feromonio_inicial,
    coeficiente_de_evaporacao,
    max_tentativas_sem_melhora,
    const_att_feromonios
)

fim = time.time()
tempo_total = fim - inicio

for i, (caminho, distancia) in enumerate(melhor_resultado):
    print(f"Motoboy {i + 1}: {' -> '.join(caminho)} | Distância: {distancia}")

print(f"\n⏱️ Tempo total de execução: {tempo_total:.2f} segundos")