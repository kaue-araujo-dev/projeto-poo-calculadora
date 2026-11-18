import tkinter as tk
from calculadora import Calculadora
from interface import CalculadoraApp

def main():
    root = tk.Tk()
    calculadora = Calculadora()
    # Passamos tanto a janela principal (root) quanto o objeto calculadora para a classe da interface
    app = CalculadoraApp(root, calculadora)
    root.mainloop()

if __name__ == "__main__":
    main()