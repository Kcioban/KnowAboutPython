# Criando um dicionário onde a chave é o nome do vendedor e o valor é o total de vendas.
vendedores = {}
for i in range(1, 11):
    nome = input(f"Nome do Vendedor {i}: ")
    vendas = int(input(f"Total de Vendas para {nome}: "))
    vendedores[nome] = vendas

# Define a meta de vendas.
meta = 10000

# Verifica se cada vendedor atingiu a meta.
for vendedor, vendas in vendedores.items():
    if vendas >= meta:
        print(f"{vendedor} atingiu a meta com {vendas} vendas.")
    else:
        print(f"{vendedor} não atingiu a meta com {vendas} vendas.")
