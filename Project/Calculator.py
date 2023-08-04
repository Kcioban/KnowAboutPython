# definições, cada opção terá um retorno
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b

# Função que recebe a operação e os números e realiza o cálculo
def calcular(operacao, a, b):
    if operacao == "+":
        return soma(a, b)
    elif operacao == "-":
        return subtracao(a, b)
    elif operacao == "*":
        return multiplicacao(a, b)
    elif operacao == "/":
        return divisao(a, b)
    else:
        return "Operação inválida."

# Exemplo de uso da calculadora
if __name__ == "__main__":
    try:
        operacao = input("Digite a operação (+, -, *, /): ")
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        resultado = calcular(operacao, numero1, numero2)

        print("Resultado:", resultado)
    except ValueError:
        print("Valores inválidos. Certifique-se de digitar números válidos.")
