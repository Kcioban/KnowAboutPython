import requests
import tkinter as tk
from   tkinter import *

# def calculo
def Fahrenheit(valorC):
    valorF = (valorC * 9/5) + 32
    return valorF

def Celsius(valorF):
    valorC = (valorF - 32) / 1.8
    return valorC

# solicitação
print("Insira o valor em Celsius e descubra em Fahrenheit")
valorC = float(input("Digite o valor em Celsius: "))

# Chame a função para calcular Fahrenheit
resultado = Fahrenheit(valorC)
print(f"{valorC} graus Celsius é igual a {resultado} graus Fahrenheit")

# definindo a estrutura visual da janela - sem alteração de tamanho
convertApp = tk.Tk()
convertApp.title("Conversao de Graus")
convertApp.resizable(False, False)
convertApp.configure(bg="000000")

value_entry    = tk.Entry(convertApp, width=10)

tk.Label(convertApp, text="Celsius:",   font=("Inter", 12, "bold"), foreground="#000000", background="#767b80", anchor="e").grid(row=2, column=0, padx=10, pady=5)
tk.Label(convertApp, text="Fahrenheit:",font=("Inter", 12, "bold"), foreground="#000000", background="#767b80", anchor="e").grid(row=2, column=0, padx=10, pady=5)

# entrada dos dados
value_entry.grid(row=0, column=1)
value_entry.configure(bg="#a9b6c1")

# Botões para ativar os calculos
celsius_entry = tk.Button(convertApp, text="Converta de C para F", command=Fahrenheit)
celsius_entry.grid(row=2, column=2, padx=10, pady=10)
celsius_entry.configure(bg="#a9b6c1")

fahrenheit_entry = tk.Button(convertApp, text="Converta de F para C", command=Celsius)
fahrenheit_entry.grid(row=2, column=3, padx=10, pady=10)
fahrenheit_entry.configure(bg="#a9b6c1")

# Mantém aberto 
convertApp.mainloop()
