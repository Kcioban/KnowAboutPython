# inserção do numero.
num = int(input("Digite um número para realizar a contagem regressiva dele: "))

print("Número atual: " + str(num))  # Convertendo num para string para poder concatená-lo

while num > 0:   # Enquanto não zerar ele decresce de 1 em 1
    print(num)
    num -= 1
