alunos = {}
for i in range(1, 6):
    nome = input(f"Nome do Aluno {i}: ")
    nota_com_virgula = input(f"Nota de {nome}: ")

    # Substitua as vírgulas por pontos
    nota_com_ponto = nota_com_virgula.replace(",", ".")

    # Converta o valor para um número de ponto flutuante
    nota = float(nota_com_ponto)
    alunos[nome] = nota

media_aprovacao = 6.0

aprovados = []
reprovados = []

for aluno, nota in alunos.items():
    if nota >= media_aprovacao:
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

print("Alunos Aprovados:")
for aluno in aprovados:
    print(f"{aluno} está aprovado.")

print("Alunos Reprovados:")
for aluno in reprovados:
    print(f"{aluno} está reprovado.")
