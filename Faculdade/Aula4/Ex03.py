# func count e separa pares
def lista_numeros_pares(numero):
    if numero < 2:
        return []  # Se o número for menor que 2, não há números pares
    else:
        return [x for x in range(2, numero + 1, 2)]

# Exemplo de uso:
numero = int(input("Digite um número inteiro positivo: "))
pares = lista_numeros_pares(numero)
print("Números pares até", numero, "são:", pares)
