def fibonacci(n):
    a, b = 0, 1
    resultado = [a]  # Inicializa lista para armazenar os resultados
    for _ in range(1, n):  # Começa do 1 para já incluir o primeiro número (0)
        a, b = b, a + b
        resultado.append(a)  # Adiciona o número atual à lista de resultados
    return resultado

# Exemplo:
n = 10
sequencia = fibonacci(n)
print(f"Sequência de Fibonacci até o {n}-ésimo número: {sequencia}")
