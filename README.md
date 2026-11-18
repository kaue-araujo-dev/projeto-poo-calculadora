# 🧮 Calculadoras Desktop em Python (Tkinter & POO)

Este repositório documenta o desenvolvimento de aplicações de calculadora em ambiente desktop utilizando **Python**, a biblioteca nativa **Tkinter** e conceitos de **Programação Orientada a Objetos (POO)**.

O projeto aborda duas variações principais focadas em portabilidade, facilidade de código limpo e arquitetura orientada a objetos.

---

## 📂 Visão Geral das Aplicações

### 1. `calculadora_com_um_arquivo` (Versão Portátil Compacta)
* **Objetivo:** Oferecer uma aplicação completa de calculadora em **um único arquivo `.py`**, facilitando o compartilhamento, backup e execução rápida.
* **Características:** 
  * Estruturada através da classe `CalculadoraSimples`.
  * Interface gráfica limpa com tema escuro (Dark Mode).
  * Gerenciamento responsivo de botões através do gerenciador de layout `grid`.
  * Atalho de teclado integrado (`Enter` para calcular instantaneamente).

### 2. `CalculadoraPOO` (Abordagem Orientada a Objetos Avançada)
* **Objetivo:** Consolidar os pilares de POO aplicados ao desenvolvimento desktop com Tkinter.
* **Características:**
  * Separação modular de responsabilidades dentro da classe principal.
  * Tratamento robusto de erros matemáticos utilizando blocos `try/except` em conjunto com a função `eval()`.
  * Suporte a eventos de teclado personalizados através do método `.bind()`.

---

## 🎨 Especificações Técnicas Comuns

* **Linguagem:** Python 3.x
* **Interface Gráfica (GUI):** `tkinter` (nativo do Python)
* **Estilização (Dark Mode):**
  * Fundo da janela: `#222`
  * Visor (Entry): `#333` com texto em `#fff`
  * Botões: `#444` com texto em negrito
* **Atalhos:** Suporte nativo à tecla `<Return>` (Enter) para acionar o cálculo.

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o **Python** instalado em sua máquina.

1. Abra o Prompt de Comando (CMD) na pasta do projeto.
2. Execute o arquivo principal da calculadora:
   ```cmd
   python main.py
