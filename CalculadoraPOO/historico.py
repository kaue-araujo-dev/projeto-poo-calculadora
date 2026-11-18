class Historico:
    def __init__(self):
        self._registros = []

    def adicionar(self, registro):
        self._registros.append(registro)

    def listar(self):
        return self._registros

    def limpar(self):
        self._registros.clear()