# 🧮 Calculadora com um Arquivo (CalculadoraPOO)

Uma calculadora desktop minimalista, moderna e 100% autossuficiente desenvolvida em **Python** utilizando **Programação Orientada a Objetos (POO)** e a biblioteca nativa **Tkinter**. 

Este projeto foi estruturado para ser limpo, leve e extremamente fácil de compilar em um único arquivo executável portátil (`.exe`) para o Windows.

## ✨ Funcionalidades Principais

* **Interface Moderna (Dark Mode):** Visual limpo em tons de cinza escuro, proporcionando conforto visual.
* **Operações Matemáticas Completas:** Suporte a adição (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`) e números decimais (`.`).
* **Suporte a Atalhos de Teclado:** Além de clicar com o mouse, você pode digitar suas expressões direto no visor e pressionar a tecla **`Enter`** para calcular o resultado instantaneamente.
* **Tratamento Inteligente de Erros:** Exibe a mensagem `"Erro"` no visor caso ocorra alguma expressão inválida ou divisão por zero, sem quebrar o programa.
* **Portabilidade Real (Single-File):** Compactado em um único arquivo executável sem dependências externas.

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Linguagem de programação)
* **Tkinter** (Biblioteca padrão para interface gráfica GUI)
* **PyInstaller** (Ferramenta de empacotamento para geração do `.exe`)

---

## 🚀 Como Executar o Projeto

Como o projeto utiliza exclusivamente bibliotecas nativas do Python, você não precisa instalar nenhuma dependência externa para rodar o código-fonte.

1. Abra o Prompt de Comando (CMD) ou PowerShell na pasta do projeto:
   ```cmd
   cd C:\Users\win 10 pro\calculadora_com_um_arquivo
   ```
2. Execute o script principal:
   ```cmd
   python main.py
   ```

---

## 📦 Como Gerar o Executável (.exe)

Se você deseja transformar o seu código em um programa independente para Windows (que roda em qualquer computador sem precisar do Python instalado), siga os passos abaixo:

1. Instale o PyInstaller (caso ainda não tenha):
   ```cmd
   python -m pip install pyinstaller
   ```

2. Execute o comando de compilação para gerar um arquivo único e ocultar a janela de terminal preta:
   ```cmd
   python -m PyInstaller --onefile --noconsole main.py
   ```

3. O seu executável pronto estará localizado dentro da pasta gerada **`dist`**:
   `dist\main.exe`

---

## 📂 Estrutura do Diretório

```text
calculadora_com_um_arquivo/
│
├── main.py          # Código-fonte completo da aplicação (Classe CalculadoraSimples)
└── README.md        # Documentação detalhada do projeto
```

## 📝 Conceitos Técnicos Aplicados

* **POO (Programação Orientada a Objetos):** Organização do código utilizando a classe `CalculadoraSimples` e métodos construtores (`__init__`).
* **Gerenciamento de Layout com Grid:** Posicionamento dinâmico dos botões com redimensionamento proporcional (`rowconfigure` e `columnconfigure`).
* **Vinculação de Eventos (`bind`):** Mapeamento da tecla `<Return>` (Enter) conectada via expressão lambda à lógica de cálculo da aplicação.