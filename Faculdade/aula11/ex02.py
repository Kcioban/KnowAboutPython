alunos = {}
for i in range(1, 6):
    nome = input(f"Nome do Aluno {i}: ")
    nota = float(input(f"Nota de {nome}: "))
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
