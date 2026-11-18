from operacoes import Soma, Subtracao, Multiplicacao, Divisao
from calculadora import Calculadora

def executar_testes():
    print("Iniciando os testes de lógica...")

    # 1. Testes das operações básicas
    assert Soma(10, 5).executar() == 15, "Falha na Adição"
    assert Subtracao(10, 5).executar() == 5, "Falha na Subtração"
    assert Multiplicacao(10, 5).executar() == 50, "Falha na Multiplicação"
    assert Divisao(10, 5).executar() == 2, "Falha na Divisão"
    print("Todas as operações matemáticas passaram!")

    # 2. Teste de divisão por zero
    try:
        Divisao(10, 0).executar()
        assert False, "Deveria ter lançado um ValueError!"
    except ValueError:
        print("Tratamento de divisão por zero funcionou corretamente!")

    # 3. Teste do Histórico e Calculadora
    calc = Calculadora()
    calc.calcular(Soma(10, 5), "+")
    calc.calcular(Subtracao(10, 5), "-")
    
    registros = calc.historico.listar()
    assert len(registros) == 2, "O histórico deveria conter exatamente 2 registros."
    print("Testes de histórico e integração passaram com sucesso!")

    print("\n🎉 Parabéns! Todos os testes de negócio passaram com êxito.")

if __name__ == "__main__":
    executar_testes()