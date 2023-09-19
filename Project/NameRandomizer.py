# biblioteca de randomização
import random

# Solicite ao usuário que insira as strings, separadas por vírgulas
entrada = input("Digite os nomes separando com vírgulas: ")

# Divida as strings inseridas pelo usuário em uma lista
nomes = entrada.split(',')

# Remova os espaços em branco em excesso em cada string
nomes = [nome.strip() for nome in nomes]

# Verifique se a lista de nomes não está vazia
if nomes:
    aux = random.choice(nomes)
    print("Nome aleatório escolhido:", aux)
else:
    print("A lista de nomes está vazia. Insira pelo menos um nome.")
