# Arquivo: produtor.py
from observer import Subject

class Produtor(Subject):
    def produzir(self, produto):
        print(f"Produtor: Produzindo {produto}")
        self.notify_observers(produto)
