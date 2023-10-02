# Biblioteca para GUI
import tkinter as tk
from tkinter import simpledialog

# Func para calcular
def calcular_media():
    n1 = simpledialog.askfloat("Solicite um número", "Digite o primeiro número: ")
    n2 = simpledialog.askfloat("Solicite um número", "Digite o segundo número: ")

    # Valida se está vazio
    if n1 is not None and n2 is not None:
        media = (n1+n2)/2
        resultado_label.config(text = f"A media dos números é: {media:.2f}")
   
    # Caso vazio, alert!
    else:
        resultado_label.config(text = "Preencha ambos os números.")

# Criar janela
janela = tk.Tk()
janela.title("Calculadora de Média")

# Criar rótulo para apresentar o resultado
resultado_label = tk.Label(janela, text=" ")
resultado_label.pack(pady=20)

# Criar um botão para solicitar os valores
botao = tk.Button(janela, text="Calcular", command=calcular_media)
botao.pack()

# Vincular a função janela.quit() para fechar a janela corretamente
janela.protocol("WM_DELETE_WINDOW", janela.quit)

# Manter a janela aberta
janela.mainloop()
