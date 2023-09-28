def fibonacci_com_loop(n):
    a, b = 0, 1
    resultado = [a]  # Inicializamos uma lista para armazenar os resultados
    for _ in range(1, n):  # Começamos de 1 para já incluir o primeiro número (0)
        a, b = b, a + b
        resultado.append(a)  # Adicionamos o número atual à lista de resultados
    return resultado

# Exemplo de uso:
n = 10
sequencia = fibonacci_com_loop(n)
print(f"Sequência de Fibonacci até o {n}-ésimo número: {sequencia}")
