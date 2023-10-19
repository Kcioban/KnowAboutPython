import  tkinter    as     tk
from    tkinter    import ttk
from    tkinter    import messagebox
from    openpyxl   import Workbook
# -------------------------------

# Função para salvar os dados em um arquivo de texto (.txt)
def salvar_em_txt():
    with open("clientes.txt", "w") as arquivo:
        for codigo, dados in clientes.items():
            linha = f"{codigo},{dados['nome']},{dados['telefone']},{dados['email']}\n"
            arquivo.write(linha)

# Função para salvar os dados em um arquivo Excel (.xlsx)
def salvar_em_excel():
    wb = Workbook()
    ws = wb.active
    ws.append(["Código", "Nome", "Telefone", "Email"])

    for codigo, dados in clientes.items():
        ws.append([codigo, dados["nome"], dados["telefone"], dados["email"]])

    wb.save("clientes.xlsx")

# Função para adicionar um novo cliente
def adicionar_cliente():
    codigo   = codigo_entry.get()
    nome     = nome_entry.get()
    telefone = telefone_entry.get()
    email    = email_entry.get()

    if codigo not in clientes:
        clientes[codigo] = {"nome": nome, "telefone": telefone, "email": email}
        lista_clientes.insert("", "end", values=(codigo, nome, telefone, email))
        limpar_campos()

# Função para editar cliente cadastrado
def editar_cliente():
    codigo = codigo_editar_entry.get()

    if codigo in clientes:
        # Cliente encontrado, exibir informações atuais
        cliente_atual = clientes[codigo]
        nome_entry.delete(0, "end")
        nome_entry.insert(0, cliente_atual["nome"])
        telefone_entry.delete(0, "end")
        telefone_entry.insert(0, cliente_atual["telefone"])
        email_entry.delete(0, "end")
        email_entry.insert(0, cliente_atual["email"])
    else:
        # Cliente não encontrado, exibir mensagem de erro
        messagebox.showerror("Erro", "Cliente não encontrado.")

# Função para atualizar o cliente
def atualizar_cliente():
    codigo = codigo_editar_entry.get()

    if codigo in clientes:
        # Atualizar informações do cliente
        clientes[codigo]["nome"]     = nome_entry.get()
        clientes[codigo]["telefone"] = telefone_entry.get()
        clientes[codigo]["email"]    = email_entry.get()

        # Limpar campos de entrada
        limpar_campos()

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
    else:
        # Cliente não encontrado, exibir mensagem de erro
        messagebox.showerror("Erro", "Cliente não encontrado.")

# Função para limpar os campos de entrada
def limpar_campos():
    codigo_entry.delete(0, "end")
    nome_entry.delete(0, "end")
    telefone_entry.delete(0, "end")
    email_entry.delete(0, "end")

# ===================================================================================================
# -------------------------------------Fim das Def's ------------------------------------------------
# ===================================================================================================

# Cria a janela & embelezamento!!!
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.resizable(False,False)
janela.configure(bg="#767b80")

# Cria variáveis para os campos de entrada
codigo_entry    = tk.Entry(janela, width=10)
nome_entry      = tk.Entry(janela, width=30)
telefone_entry  = tk.Entry(janela, width=15)
email_entry     = tk.Entry(janela, width=30)

# Cria rótulos para os campos
tk.Label(janela, text="Código:",   font=("Inter", 12, "bold"), foreground="#000000", background="#767b80", anchor="e").grid(row=0, column=0, padx=10, pady=5)
tk.Label(janela, text="Nome:",     font=("Inter", 12, "bold"), foreground="#000000", background="#767b80", anchor="e").grid(row=1, column=0, padx=10, pady=5)
tk.Label(janela, text="Telefone:", font=("Inter", 12, "bold"), foreground="#000000", background="#767b80", anchor="e").grid(row=2, column=0, padx=10, pady=5)
tk.Label(janela, text="Email:",    font=("Inter", 12, "bold"), foreground="#000000", background="#767b80", anchor="e").grid(row=3, column=0, padx=10, pady=5)

# Posiciona os campos de entrada
codigo_entry.grid(row=0, column=1)
codigo_entry.configure(bg="#a9b6c1")

nome_entry.grid(row=1, column=1)
nome_entry.configure(bg="#a9b6c1")

telefone_entry.grid(row=2, column=1)
telefone_entry.configure(bg="#a9b6c1")

email_entry.grid(row=3, column=1)
email_entry.configure(bg="#a9b6c1")

# Cria um botão para adicionar um novo cliente
adicionar_botao = tk.Button(janela, text="Adicionar Cliente", command=adicionar_cliente)
adicionar_botao.grid(row=4, column=1, padx=10, pady=10)
adicionar_botao.configure(bg="#a9b6c1")

# Botão para pesquisar e editar um cliente
editar_botao = tk.Button(janela, text="Editar Cliente", command=editar_cliente)
editar_botao.grid(row=5, column=0, padx=5, pady=5)
editar_botao.configure(bg="#a9b6c1")

# Campo de entrada para código de edição
codigo_editar_entry = tk.Entry(janela, width=10)
codigo_editar_entry.grid(row=5, column=1, padx=5, pady=5)
codigo_editar_entry.configure(bg="#a9b6c1")

# Botão para atualizar as informações do cliente
atualizar_botao = tk.Button(janela, text="Atualizar Cliente", command=atualizar_cliente)
atualizar_botao.grid(row=4, column=0, padx=5, pady=5)
atualizar_botao.configure(bg="#a9b6c1")

# Cria uma lista de clientes
lista_clientes = ttk.Treeview(janela, columns=("Código", "Nome", "Telefone", "Email"), show="headings")
lista_clientes.heading("Código", text="Código")
lista_clientes.heading("Nome", text="Nome")
lista_clientes.heading("Telefone", text="Telefone")
lista_clientes.heading("Email", text="Email")
lista_clientes.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Cria botões para salvar em TXT 
salvar_txt_botao = tk.Button(janela, text="Salvar em TXT", command=salvar_em_txt)
salvar_txt_botao.grid(row=6, column=0, padx=10, pady=10)
salvar_txt_botao.configure(bg="#a9b6c1")

# Cria botões para salvar em Excel.xlsx
salvar_excel_botao = tk.Button(janela, text="Salvar em Excel", command=salvar_em_excel)
salvar_excel_botao.grid(row=6, column=1, padx=5, pady=5)
salvar_excel_botao.configure(bg="#a9b6c1")

# Dicionário para armazenar os clientes (código como chave e dados como valor)
clientes = {}

# Inicia a interface e mantém ela aberta
janela.mainloop()
