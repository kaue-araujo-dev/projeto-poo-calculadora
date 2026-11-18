# 🧮 CalculadoraPOO

Uma calculadora desktop simples, moderna e leve desenvolvida em **Python** utilizando **Programação Orientada a Objetos (POO)** e a biblioteca nativa **Tkinter**.

---

## ✨ Funcionalidades

* **Operações Básicas:** Adição (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`), com suporte a números decimais (`.`).
* **Suporte a Teclado:** Além dos cliques com o mouse, permite digitar expressões diretamente no visor e pressionar a tecla **`Enter`** para obter o resultado instantaneamente.
* **Interface Minimalista (Dark Mode):** Design limpo, responsivo e com tema escuro.
* **Tratamento de Erros:** Exibe a mensagem `"Erro"` no visor caso uma expressão inválida ou divisão por zero seja inserida.
* **Portabilidade:** Preparada para ser compilada em um único arquivo executável (`.exe`) portátil para Windows.

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3](https://www.python.org/):** Linguagem principal do projeto.
* **[Tkinter](https://docs.python.org/3/library/tkinter.html):** Biblioteca padrão do Python para criação da interface gráfica (GUI).
* **[PyInstaller](https://pyinstaller.org/):** Ferramenta utilizada para empacotar a aplicação em um executável independente.

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o **Python 3** instalado em sua máquina. Como o `tkinter` já faz parte da biblioteca padrão do Python na maioria das instalações (especialmente no Windows), não é necessário instalar dependências externas para rodar o código-fonte.

### 2. Rodando via Terminal
Clone ou baixe os arquivos do projeto, abra o terminal (CMD ou PowerShell) na pasta raiz e execute:

```bash
python main.py
```

---

## 📦 Gerando o Executável (.exe)

Caso queira distribuir a calculadora como um programa independente para Windows (sem precisar que o usuário tenha o Python instalado):

1. Instale o **PyInstaller**:
   ```bash
   python -m pip install pyinstaller
   ```

2. Execute o comando de compilação para gerar um arquivo único sem a janela de terminal ao fundo:
   ```bash
   python -m PyInstaller --onefile --noconsole main.py
   ```

3. O executável final (`main.exe`) estará disponível dentro da pasta **`dist/`**.

---

## 📂 Estrutura do Projeto

```text
CalculadoraPOO/
│
├── main.py          # Código-fonte principal da aplicação (Classe CalculadoraSimples)
└── README.md        # Documentação do projeto
```

---

## 📝 Aprendizados e Conceitos Aplicados

* Estruturação de interfaces gráficas utilizando classes e métodos (**POO**).
* Gerenciamento de layout em grade (`grid`) e redimensionamento responsivo (`rowconfigure` / `columnconfigure`).
* Captura e vinculação de eventos de teclado utilizando o método `.bind("<Return>")`.
* Empacotamento de scripts Python para distribuição em ambiente Windows.