# Arquivo: consumidor.py
from observer import Observer

class Consumidor(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, message):
        print(f"{self.nome} recebeu o produto: {message}")
