import tkinter as tk
from tkinter import messagebox, scrolledtext
from operacoes import Soma, Subtracao, Multiplicacao, Divisao

class CalculadoraApp:
    def __init__(self, root, calculadora):
        self.root = root
        self.root.title("Calculadora POO")
        self.root.geometry("400x520")
        self.root.resizable(False, False)
        
        self.calculadora = calculadora
        
        self.criar_widgets()

    def criar_widgets(self):
        # Frame de Entrada de Dados
        frame_inputs = tk.LabelFrame(self.root, text="Valores", font=("Arial", 10, "bold"), padx=10, pady=10)
        frame_inputs.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_inputs, text="Primeiro número:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_primeiro = tk.Entry(frame_inputs, font=("Arial", 12), width=15)
        self.entry_primeiro.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_inputs, text="Segundo número:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_segundo = tk.Entry(frame_inputs, font=("Arial", 12), width=15)
        self.entry_segundo.grid(row=1, column=1, padx=10, pady=5)

        # Frame de Operações (Botões)
        frame_botoes = tk.LabelFrame(self.root, text="Operações", font=("Arial", 10, "bold"), padx=10, pady=10)
        frame_botoes.pack(fill="x", padx=15, pady=5)

        btn_soma = tk.Button(frame_botoes, text="Somar (+)", font=("Arial", 10), bg="#e0e0e0", width=12, command=lambda: self.realizar_calculo(Soma, "+"))
        btn_soma.grid(row=0, column=0, padx=5, pady=5)

        btn_sub = tk.Button(frame_botoes, text="Subtrair (-)", font=("Arial", 10), bg="#e0e0e0", width=12, command=lambda: self.realizar_calculo(Subtracao, "-"))
        btn_sub.grid(row=0, column=1, padx=5, pady=5)

        btn_mult = tk.Button(frame_botoes, text="Multiplicar (×)", font=("Arial", 10), bg="#e0e0e0", width=12, command=lambda: self.realizar_calculo(Multiplicacao, "×"))
        btn_mult.grid(row=1, column=0, padx=5, pady=5)

        btn_div = tk.Button(frame_botoes, text="Dividir (÷)", font=("Arial", 10), bg="#e0e0e0", width=12, command=lambda: self.realizar_calculo(Divisao, "÷"))
        btn_div.grid(row=1, column=1, padx=5, pady=5)

        # Exibição de Resultado
        frame_resultado = tk.Frame(self.root, padx=15, pady=5)
        frame_resultado.pack(fill="x")
        
        tk.Label(frame_resultado, text="Resultado:", font=("Arial", 11, "bold")).pack(anchor="w")
        self.lbl_resultado = tk.Label(frame_resultado, text="", font=("Arial", 14, "bold"), fg="blue")
        self.lbl_resultado.pack(anchor="w", pady=2)

        # Histórico e Limpeza
        frame_historico = tk.LabelFrame(self.root, text="Histórico", font=("Arial", 10, "bold"), padx=10, pady=5)
        frame_historico.pack(fill="both", expand=True, padx=15, pady=10)

        self.txt_historico = scrolledtext.ScrolledText(frame_historico, height=5, font=("Arial", 9), state="disabled")
        self.txt_historico.pack(fill="both", expand=True, pady=5)

        # Botões de Ação Inferiores (Limpar campos e histórico)
        frame_acoes = tk.Frame(self.root, padx=15, pady=5)
        frame_acoes.pack(fill="x", pady=5)

        btn_limpar_campos = tk.Button(frame_acoes, text="Limpar Campos", font=("Arial", 9), command=self.limpar_campos)
        btn_limpar_campos.pack(side="left", expand=True, fill="x", padx=2)

        btn_limpar_hist = tk.Button(frame_acoes, text="Limpar Histórico", font=("Arial", 9), command=self.limpar_historico)
        btn_limpar_hist.pack(side="right", expand=True, fill="x", padx=2)

    def realizar_calculo(self, classe_operacao, simbolo):
        try:
            # Converte as entradas para float e trata erros de preenchimento
            val1 = float(self.entry_primeiro.get())
            val2 = float(self.entry_segundo.get())

            # Instancia o objeto de operação específico
            operacao = classe_operacao(val1, val2)

            # Delega o cálculo para a classe Calculadora (que gerencia o histórico)
            resultado = self.calculadora.calcular(operacao, simbolo)

            # Formata a exibição do resultado se for inteiro
            res_formatado = int(resultado) if isinstance(resultado, float) and resultado.is_integer() else resultado
            self.lbl_resultado.config(text=str(res_formatado))

            # Atualiza a visualização do histórico na interface
            self.atualizar_visor_historico()

        except ValueError as erro:
            # Captura tanto erro de conversão de texto quanto o ValueError de divisão por zero
            mensagem = str(erro) if "Divisão" in str(erro) else "Digite valores numéricos válidos."
            messagebox.showerror("Erro de Validação", mensagem)

    def atualizar_visor_historico(self):
        self.txt_historico.config(state="normal")
        self.txt_historico.delete("1.0", tk.END)
        registros = self.calculadora.historico.listar()
        # Exibe os registros mais recentes no topo ou em ordem sequencial
        for reg in registros:
            self.txt_historico.insert(tk.END, reg + "\n")
        self.txt_historico.config(state="disabled")

    def limpar_campos(self):
        self.entry_primeiro.delete(0, tk.END)
        self.entry_segundo.delete(0, tk.END)
        self.lbl_resultado.config(text="")

    def limpar_historico(self):
        self.calculadora.historico.limpar()
        self.atualizar_visor_historico()