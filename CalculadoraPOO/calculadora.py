from historico import Historico

class Calculadora:
    def __init__(self, historico=None):
        # Permite receber um objeto Historico existente ou criar um novo por padrão
        self.historico = historico if historico is not None else Historico()

    def calcular(self, operacao, simbolo):
        # 1. Executa a operação usando polimorfismo (método herdado)
        resultado = operacao.executar()
        
        # Opcional: formata os números para remover o '.0' caso sejam inteiros (melhora a exibição)
        p = int(operacao._primeiro) if operacao._primeiro.is_integer() else operacao._primeiro
        s = int(operacao._segundo) if operacao._segundo.is_integer() else operacao._segundo
        res = int(resultado) if isinstance(resultado, float) and resultado.is_integer() else resultado

        # 2 e 3. Monta a expressão formatada e registra no histórico
        registro = f"{p} {simbolo} {s} = {res}"
        self.historico.adicionar(registro)
        
        # 4. Devolve o resultado da operação
        return resultado