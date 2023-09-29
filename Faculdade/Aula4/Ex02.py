# def calculo
def Fahrenheit(valorC):
    valorF = (valorC * 9/5) + 32
    return valorF

#solicitação
print("Insira o valor em Celsius e descubra em Fahrenheit")
valorC = float(input("Digite o valor em Celsius: "))

# Chame a função para calcular Fahrenheit
resultado = Fahrenheit(valorC)
print(f"{valorC} graus Celsius é igual a {resultado} graus Fahrenheit")
