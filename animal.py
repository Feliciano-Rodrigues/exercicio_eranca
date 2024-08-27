# animal.py
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def movimentar(self):
        pass
