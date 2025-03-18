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
        self.visitados = set()  # Para controlar os pontos já visitados

    def escolher_rota(self, ponto_atual: Ponto) -> TabelaDeProbabilidades:
        # Calcular probabilidades para o próximo ponto
        probabilidades = [tabela for tabela in self.tabela_de_probabilidades if tabela.rota.startswith(f"{ponto_atual.nome} ->")]
        
        # Filtrar rotas já visitadas
        probabilidades = [tabela for tabela in probabilidades if ponto_atual.nome != tabela.rota.split(" -> ")[1] and tabela.rota.split(" -> ")[1] not in self.visitados]

        # Se não houver mais opções válidas (todos os pontos foram visitados), a formiga volta ao início
        if not probabilidades:
            # Escolher a rota de volta ao ponto inicial
            tabela_retorno = next(tabela for tabela in self.tabela_de_probabilidades if tabela.rota.startswith(f"{ponto_atual.nome} -> {self.pontos[0].nome}"))
            return tabela_retorno

        # Normalizar as probabilidades
        soma_probabilidades = sum([tabela.probabilidade for tabela in probabilidades])
        
        if soma_probabilidades > 0:
            # Escolher a próxima rota com base nas probabilidades
            escolha = random.choices(probabilidades, weights=[tabela.probabilidade for tabela in probabilidades], k=1)[0]
        else:
            # Caso não haja probabilidades (devido a falta de opções), escolher aleatoriamente
            escolha = random.choice(probabilidades)
        
        return escolha

    def percorrer(self):
        # Começar da primeira cidade
        ponto_atual = self.pontos[0]
        self.visitados.add(ponto_atual.nome)  # Marcar o ponto inicial como visitado
        self.caminho.append(f"{ponto_atual.nome}")  # Inicializa o caminho com o ponto inicial
        
        while len(self.visitados) < len(self.pontos):  # Enquanto não tiver visitado todos os pontos
            tabela = self.escolher_rota(ponto_atual)
            self.caminho.append(f"-> {tabela.rota.split(' -> ')[1]}")  # Apenas registrando o próximo ponto
            self.distancia_total += tabela.distancia
            self.feromonios_depositados.append(tabela)
            ponto_atual = self.pontos[self.pontos.index(ponto_atual) + 1] if tabela.rota.split(" -> ")[1] != self.pontos[0].nome else self.pontos[0]  # Próximo ponto (se não for o inicial) ou volta ao inicial
            self.visitados.add(tabela.rota.split(" -> ")[1])  # Marcar o ponto como visitado
        
        # Após percorrer todos os pontos, voltar ao ponto inicial
        tabela_retorno = next(tabela for tabela in self.tabela_de_probabilidades if tabela.rota.startswith(f"{ponto_atual.nome} -> {self.pontos[0].nome}"))
        self.caminho.append(f"-> {self.pontos[0].nome}")  # Adiciona o retorno ao ponto inicial
        self.distancia_total += tabela_retorno.distancia
        self.feromonios_depositados.append(tabela_retorno)
