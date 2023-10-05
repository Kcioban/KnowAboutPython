import  tkinter as tk
from    tkinter import *

# Função para atualizar o display
def btn_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Função para realizar cálculos
def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro!")

# Função para limpar o display
def clear():
    entry.delete(0, tk.END)

# Cria a janela principal
window = tk.Tk()
window.title("Calculadora")

# Criando um widget de entrada para o display
entry = tk.Entry(window, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Botões de números e operações
btn_1 = tk.Button(window, text="1", padx=20, pady=20, command=lambda: btn_click(1))
btn_2 = tk.Button(window, text="2", padx=20, pady=20, command=lambda: btn_click(2))
btn_3 = tk.Button(window, text="3", padx=20, pady=20, command=lambda: btn_click(3))
btn_4 = tk.Button(window, text="4", padx=20, pady=20, command=lambda: btn_click(4))
btn_5 = tk.Button(window, text="5", padx=20, pady=20, command=lambda: btn_click(5))
btn_6 = tk.Button(window, text="6", padx=20, pady=20, command=lambda: btn_click(6))
btn_7 = tk.Button(window, text="7", padx=20, pady=20, command=lambda: btn_click(7))
btn_8 = tk.Button(window, text="8", padx=20, pady=20, command=lambda: btn_click(8))
btn_9 = tk.Button(window, text="9", padx=20, pady=20, command=lambda: btn_click(9))
btn_0 = tk.Button(window, text="0", padx=20, pady=20, command=lambda: btn_click(0))

btn_add     = tk.Button(window, text="+", padx=20, pady=20, command=lambda: btn_click("+"))
btn_sub     = tk.Button(window, text="-", padx=20, pady=20, command=lambda: btn_click("-"))
btn_mult    = tk.Button(window, text="*", padx=20, pady=20, command=lambda: btn_click("*"))
btn_div     = tk.Button(window, text="/", padx=20, pady=20, command=lambda: btn_click("/"))
btn_equals  = tk.Button(window, text="=", padx=20, pady=20, command=calculate)
btn_clear   = tk.Button(window, text="C", padx=20, pady=20, command=clear)

# Posicionamento dos botões
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_add.grid(row=1, column=3)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_mult.grid(row=3, column=3)

btn_0.grid(row=4, column=0)
btn_div.grid(row=4, column=1)
btn_clear.grid(row=4, column=2)
btn_equals.grid(row=4, column=3)

# Inicia o loop 
window.mainloop()
