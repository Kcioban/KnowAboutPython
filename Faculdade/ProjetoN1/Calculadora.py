import tkinter as tk

botoes_numeros = [(1, 30, 280), (2, 90, 280), (3, 150, 280), (4, 30, 220), (5, 90, 220), (6, 150, 220), (7, 30, 160), (8, 90, 160), (9, 150, 160), (0, 30, 340)]
botoes_operadores = [("/", 160), ("*", 220), ("-", 280), ("+", 340)]
calculo = str()

# Funções.
def adicionar_numero(numero: str):
    global calculo
    calculo += numero
    texto_calculo.config(text=calculo)

def adicionar_operador(operador: str):
    global calculo
    calculo += operador
    texto_calculo.config(text=calculo)

def calcular():
    global calculo
    resultado = round(eval(calculo), 2)
    texto_resultado.config(text=resultado)
    calculo = str(resultado)

def clear():
    global calculo
    calculo = ""  # Defina a variável 'calculo' como uma string vazia
    texto_calculo.config(text=calculo)
    texto_resultado.config(text=calculo)

# Configuração da Janela.
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x430")
janela.resizable(False, False)
janela.configure(background="#292c30")

# Frame da Tela.
tela = tk.Frame(janela, background="#323538", relief="flat")
tela.place(x=30, y=40, width=240, height=100)

# Texto do Calculo.
texto_calculo = tk.Label(tela, text="", font=("arial", 12, "bold"), foreground="#767b80", background="#323538", anchor="e")
texto_calculo.place(x=20, y=20, width=200)

# Texto do Resultado.
texto_resultado = tk.Label(tela, text="", font=("arial", 20, "bold"), foreground="#ffffff", background="#323538", anchor="e")
texto_resultado.place(x=20, y=50, width=200)

# Loop Numeros.
for (numero, x, y) in botoes_numeros:
    botao = tk.Button(janela, text=f"{numero}", font=("arial", 10, "normal"), background="#406285", foreground="#ffffff", relief="flat", highlightthickness=0, command=lambda num=numero: adicionar_numero(f"{num}"))
    botao.place(x=x, y=y, width=50, height=50)

# Loop Operadores.
for (operador, y) in botoes_operadores:
    botao = tk.Button(janela, text=f"{operador}", font=("arial", 10, "normal"), background="#a36a00", foreground="#ffffff", relief="flat", highlightthickness=0, command=lambda ope=operador: adicionar_operador(f" {ope} "))
    botao.place(x=210, y=y, width=50, height=50)

# Botão de Igual.
botao = tk.Button(janela, text="=", font=("arial", 10, "normal"), background="#a36a00", foreground="#ffffff", relief="flat", highlightthickness=0, command=calcular)
botao.place(x=150, y=340, width=50, height=50)

# Botão Limpar/Clear
botao = tk.Button(janela, text="C", font=("arial", 10, "normal"), background="#a36a00", foreground="#ffffff", relief="flat", highlightthickness=0, command=clear)
botao.place(x=90, y=340, width=50, height=50)

# Mainloop.
janela.mainloop()
