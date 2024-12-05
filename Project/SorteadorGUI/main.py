import tkinter as tk
root = tk.Tk()

imagem = tk.PhotoImage(file="c:/Users/Public---ALTERAR PATH---Pictures/stack-overflow.png")
w = tk.Label(root, image=imagem)
w.imagem = imagem
w.pack()

root.mainloop()
