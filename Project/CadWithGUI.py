# Biblioteca para GUI(Ui/Ux)
import tkinter as tk
from tkinter import messagebox

# Criando um objeto e atribuindo propriedades, no caso um 'nome' e 'idade'
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Array para armazenar 
pessoas = []

# Limpar dados da janela
def limpar_entrada():
    entrada.delete(0, tk.END)

# Função criação
def criar_pessoa():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    pessoa = Pessoa(nome, idade)
    pessoas.append(pessoa)
    messagebox.showinfo("Sucesso", "Pessoa criada com sucesso!")
    limpar_entrada()

# Função listagem
def listar_pessoas():
    if not pessoas:
        messagebox.showinfo("Lista de Pessoas", "Nenhuma pessoa cadastrada.")
    else:
        lista = "Lista de pessoas:\n"
        for pessoa in pessoas:
            lista += f"Nome: {pessoa.nome}, Idade: {pessoa.idade}\n"
        messagebox.showinfo("Lista de Pessoas", lista)

# Função atualização
def atualizar_pessoa():
    nome = nome_entry.get()
    encontrou = False
    for pessoa in pessoas:
        if pessoa.nome == nome:
            novo_nome = novo_nome_entry.get()
            nova_idade = int(nova_idade_entry.get())
            pessoa.nome = novo_nome
            pessoa.idade = nova_idade
            encontrou = True
            messagebox.showinfo("Sucesso", "Pessoa atualizada com sucesso!")
            break
    if not encontrou:
        messagebox.showerror("Erro", "Pessoa não encontrada.")

# Função deletar
def deletar_pessoa():
    nome = nome_entry.get()
    encontrou = False
    for pessoa in pessoas:
        if pessoa.nome == nome:
            pessoas.remove(pessoa)
            encontrou = True
            messagebox.showinfo("Sucesso", "Pessoa deletada com sucesso!")
            break
    if not encontrou:
        messagebox.showerror("Erro", "Pessoa não encontrada.")

# Criando a janela principal (root)
root = tk.Tk()
root.title("Cadastro de Pessoas")

# Rotulo / texto - nome
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()

# input nome - criar pessoa 
nome_entry = tk.Entry(root)
nome_entry.pack()

# Rotulo / texto - idade
idade_label = tk.Label(root, text="Idade:")
idade_label.pack()

# input idade - criar pessoa 
idade_entry = tk.Entry(root)
idade_entry.pack()

# Push botton para incluir
criar_button = tk.Button(root, text="Criar Pessoa", command=criar_pessoa)
criar_button.pack()

# Push botton - pop-up lista
listar_button = tk.Button(root, text="Listar Pessoas", command=listar_pessoas)
listar_button.pack()

# Rotulo / texto - atualização pessoa 
novo_nome_label = tk.Label(root, text="Novo Nome:")
novo_nome_label.pack()

# input - nova pessoa 
novo_nome_entry = tk.Entry(root)

