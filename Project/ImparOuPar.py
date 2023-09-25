# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro e descubra se ele é impar ou par: "))

# Verificação do número, se é par ou ímpar
if numero % 2 == 0:
    print(numero, "é um número par.")
else:
    print(numero, "é um número ímpar.")
