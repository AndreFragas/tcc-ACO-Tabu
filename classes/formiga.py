import random
from typing import List
from classes.ponto import Ponto
from classes.tabela_probabilidades import TabelaDeProbabilidades

class Formiga():
    def __init__(self, pontos: List[Ponto], tabela_de_probabilidades: List[TabelaDeProbabilidades]):
        self.pontos = pontos
        self.tabela_de_probabilidades = tabela_de_probabilidades
        self.caminho = []
        self.distancia_total = 0
        self.feromonios_depositados = []
        self.visitados = set()

    def escolher_rota(self, ponto_atual: Ponto) -> TabelaDeProbabilidades:
        probabilidades = [tabela for tabela in self.tabela_de_probabilidades if tabela.rota.startswith(f"{ponto_atual.nome} ->")]
        probabilidades = [tabela for tabela in probabilidades if ponto_atual.nome != tabela.rota.split(" -> ")[1] and tabela.rota.split(" -> ")[1] not in self.visitados]

        if not probabilidades:
            tabela_retorno = next(tabela for tabela in self.tabela_de_probabilidades if tabela.rota.startswith(f"{ponto_atual.nome} -> {self.pontos[0].nome}"))
            return tabela_retorno

        soma_probabilidades = sum([tabela.probabilidade for tabela in probabilidades])
        
        if soma_probabilidades > 0:
            escolha = random.choices(probabilidades, weights=[tabela.probabilidade for tabela in probabilidades], k=1)[0]
        else:
            escolha = random.choice(probabilidades)
        
        return escolha

    def percorrer(self):
        ponto_atual = self.pontos[0]
        self.visitados.add(ponto_atual.nome)  
        self.caminho.append(f"{ponto_atual.nome}")
        rotas_percorridas = []

        while len(self.visitados) < len(self.pontos):
            tabela = self.escolher_rota(ponto_atual)
            self.caminho.append(f"-> {tabela.rota.split(' -> ')[1]}")
            self.distancia_total += tabela.distancia
            self.feromonios_depositados.append(tabela)
            rotas_percorridas.append(tabela)
            ponto_atual = self.pontos[self.pontos.index(ponto_atual) + 1] if tabela.rota.split(" -> ")[1] != self.pontos[0].nome else self.pontos[0]
            self.visitados.add(tabela.rota.split(" -> ")[1]) 

        tabela_retorno = rotas_percorridas[-1]  
        self.caminho.append(f"-> {self.pontos[0].nome}")  
        self.distancia_total += tabela_retorno.distancia
        self.feromonios_depositados.append(tabela_retorno)

