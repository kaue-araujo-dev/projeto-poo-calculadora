import tkinter as tk


class CalculadoraSimples:

  def __init__(self, root):
    self.root = root
    self.root.title("Calculadora")
    self.root.geometry("300x400")
    self.root.config(bg="#222")

    # Variável que guarda o texto da tela
    self.expressao = tk.StringVar()

    # Campo de Texto (Visor)
    visor = tk.Entry(
        root,
        textvariable=self.expressao,
        font=("Arial", 20),
        justify="right",
        bd=0,
        bg="#333",
        fg="#fff",
    )
    visor.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

    # Atalho para calcular ao pressionar a tecla Enter do teclado
    self.root.bind("<Return>", lambda event: self.clique("="))

    # Grade de Botões
    botoes = [
        ("C", 1, 0),
        ("/", 1, 1),
        ("*", 1, 2),
        ("-", 1, 3),
        ("7", 2, 0),
        ("8", 2, 1),
        ("9", 2, 2),
        ("+", 2, 3),
        ("4", 3, 0),
        ("5", 3, 1),
        ("6", 3, 2),
        ("=", 3, 3),
        ("1", 4, 0),
        ("2", 4, 1),
        ("3", 4, 2),
        ("0", 5, 0),
        (".", 5, 1),
    ]

    # Criando um frame para os botões
    quadro = tk.Frame(root, bg="#222")
    quadro.pack(expand=True, fill="both", padx=10, pady=10)

    for texto, linha, coluna in botoes:
      cmd = lambda t=texto: self.clique(t)
      btn = tk.Button(
          quadro,
          text=texto,
          font=("Arial", 14, "bold"),
          bg="#444",
          fg="#fff",
          bd=0,
          command=cmd,
      )
      # Posicionamento simples em grid
      if texto == "=":
        btn.grid(row=linha, column=coluna, rowspan=2, sticky="nsew", padx=2, pady=2)
      else:
        btn.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

    # Configurar peso das linhas/colunas do grid para redimensionar bem
    for i in range(6):
      quadro.rowconfigure(i, weight=1)
    for i in range(4):
      quadro.columnconfigure(i, weight=1)

  def clique(self, valor):
    if valor == "C":
      self.expressao.set("")
    elif valor == "=":
      try:
        resultado = str(eval(self.expressao.get()))
        self.expressao.set(resultado)
      except Exception:
        self.expressao.set("Erro")
    else:
      self.expressao.set(self.expressao.get() + valor)


if __name__ == "__main__":
  root = tk.Tk()
  app = CalculadoraSimples(root)
  root.mainloop()