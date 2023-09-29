# Constante para o valor da aprovação
NOTA_APROVACAO = 6.0

nota1 = float(input("Informe a primeira nota:\n"))
nota2 = float(input("Informe a segunda nota:\n"))

# Função para calcular a média
def calcularMedia(n1, n2):
    return (n1 + n2) / 2

media = calcularMedia(nota1, nota2)
print("Sua média foi de:", media)
