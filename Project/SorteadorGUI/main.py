import tkinter as tk
root = tk.Tk()

# Import da biblioteca de randomização
import random

proximo_numero = 1  # Variável global inicializada com 1

def add_pessoas_lista(lista_nomes):
    """Adiciona pessoas à lista a partir de uma lista de nomes.
    Args:
        lista_nomes (list): Lista de nomes a serem adicionados.
    """

    for nome in lista_nomes:
        numero = int(numero.get())  # Assumindo que numero.get() retorna o próximo número
        pessoa = Pessoa(nome, numero)
        pessoas.append(pessoa)
        messagebox.showinfo("Sucesso", "Pessoa criada com sucesso!")
        limpar_entrada()

# Lista de nomes pronta
nomes = [“Ana Cristina Ferreira”, “Andréia Lima”, “Euclemes Junior”, “Bruno Leonardo Bertazzi”, “Caique Aparecido Dos Santos”, “Claudio Henrique Fortunato”, “Daiane De Souza Da Silva”, “Danilo Freire”, “Elisangela Almeida”, “Felipe Rovaris Leme”, “Fernando Henrique Bárbaro”, “Flavio Alves Leme”, “Gabriel Ferreira Francisco”, “George De Paula Cristiani”, “Heros Mello”, “Hugo Drago”, “Iasmim Rodrigues da Silva”, “Iranildo Melzani Ferreira”, “Isabela Casagrande Pazinatti”, “Jade Fernanda da Silva Luiz”, “Jose Pereira da Silva Junior”, “Juliano Divino Ramos”, “Julio Cesar Firmiano De Moraes”, “Juscelino Silva”, “Kauane Beatriz Da Silva”, “Kayky Cioban Nakagawa”, “Leandro Aires De Souza”, “Leonam Barbosa”, “Luanda Almeida Antunes”, “Lucas Barbosa Ramos”, “Marcelo Domingues De Souza”, “Marco Tulio Andrade”, “Maria Eduarda Cunha”, “Maria Tereza”, “Mateus Marchesini”, “Nara Borges”, “Nicoli Da Silva Oliveira”, “Paul Cleveland”, “Paulo Eiclher”, “Pedro Henrique Flores”, “Pedro Henrique Rodrigues”, “Raniel Ribeiro”, “Raphael Da Silva Araujo”, “Renato Mendes Barros”, “Rosangela Lourdes Ferreira”, “Samir Rogério Costa”, “Stefani Scareli”, “Tamires Cassia Duo Madeira”, “Vitor Hugo Serigatti”, “Vitor Tarik Colinski Pereira”, “Vivian Cristina Firmino”, “Wesley Alexandre De Carvalho”, “Wesley Oliveira”]

rand.

imagem = tk.PhotoImage(file="c:/Users/Public---ALTERAR PATH---Pictures/stack-overflow.png")
w = tk.Label(root, image=imagem)
w.imagem = imagem
w.pack()

root.mainloop()
