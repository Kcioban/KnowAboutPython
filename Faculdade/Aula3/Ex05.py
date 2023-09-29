# Solicita um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é negativo
if numero < 0:
    print("Fatorial é indefinido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    contador = 1
    while contador <= numero:
        fatorial *= contador
        contador += 1
    print(f"O fatorial de {numero} é {fatorial}")
