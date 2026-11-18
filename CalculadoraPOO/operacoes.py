from abc import ABC, abstractmethod

class Operacao(ABC):
    def __init__(self, primeiro, segundo):
        self._primeiro = float(primeiro)
        self._segundo = float(segundo)

    @abstractmethod
    def executar(self):
        pass

class Soma(Operacao):
    def executar(self):
        return self._primeiro + self._segundo

class Subtracao(Operacao):
    def executar(self):
        return self._primeiro - self._segundo

class Multiplicacao(Operacao):
    def executar(self):
        return self._primeiro * self._segundo

class Divisao(Operacao):
    def executar(self):
        if self._segundo == 0:
            raise ValueError("Erro: Divisão por zero não é permitida.")
        return self._primeiro / self._segundo