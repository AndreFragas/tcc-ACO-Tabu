class TabelaDeProbabilidades():
    def __init__(self, rota: str, distancia: float, feromonio_inicial: float, coeficiente_de_evaporacao: float):
        self.rota = rota
        self.distancia = distancia
        self.inverso_distancia = 1 / distancia
        self.feromonio = feromonio_inicial
        self.coeficiente_de_evaporacao = coeficiente_de_evaporacao
        self.relacao = self.inverso_distancia * self.feromonio
        self.probabilidade = 0
        self.probabilidade_porcentagem = 0

    def calcularProbabilidade(self, relacoes: list[float]):
        soma_relacoes = sum(relacoes)
        self.probabilidade = self.relacao / soma_relacoes
        self.probabilidade_porcentagem = self.probabilidade * 100

    def atualizarFeromonio(self, delta_feromonio: float):
        self.feromonio *= (1 - self.coeficiente_de_evaporacao)
        self.feromonio += delta_feromonio
        self.relacao = self.inverso_distancia * self.feromonio


