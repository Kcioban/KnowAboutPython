import tkinter as tk

def Fahrenheit():
    try:
        valorC = float(value_entry.get())
        valorF = (valorC * 9/5) + 32
        result_label.config(
            text=f"{valorC} graus Celsius é igual a {valorF} graus Fahrenheit")
    except ValueError:
        result_label.config(text="Valor inválido")

def Celsius():
    try:
        valorF = float(value_entry.get())
        valorC = (valorF - 32) / 1.8
        result_label.config(
            text=f"{valorF} graus Fahrenheit é igual a {valorC} graus Celsius")
    except ValueError:
        result_label.config(text="Valor inválido")

convertApp = tk.Tk()
convertApp.title("Conversao de Graus")
convertApp.resizable(False, False)
convertApp.configure(bg="#000000")

value_entry = tk.Entry(convertApp, width=10)
value_entry.grid(row=0, column=1)
value_entry.configure(bg="#a9b6c1")

celsius_entry = tk.Button(convertApp, text="Converta de C para F", command=Fahrenheit)
celsius_entry.grid(row=1, column=0, padx=10, pady=10)
celsius_entry.configure(bg="#a9b6c1")

fahrenheit_entry = tk.Button(convertApp, text="Converta de F para C", command=Celsius)
fahrenheit_entry.grid(row=1, column=1, padx=10, pady=10)
fahrenheit_entry.configure(bg="#a9b6c1")

result_label = tk.Label(convertApp, text="", font=("Inter", 12, "bold"), foreground="#000000", background="#767b80")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')

convertApp.mainloop()
