total_alunos = 500
quantidade_eleitores = 0
soma_nao_eleitores = 0
quantidade_nao_eleitores = 0

for i in range(1, total_alunos + 1):
    idade = int(input(f"Digite a idade do aluno {i}: "))
    
    if idade >= 16:
        quantidade_eleitores += 1
    else:
        quantidade_nao_eleitores += 1
        soma_nao_eleitores += idade

if quantidade_nao_eleitores > 0:
    media_nao_eleitores = soma_nao_eleitores / quantidade_nao_eleitores
else:
    media_nao_eleitores = 0

print("\nResultados:")
print(f"Quantidade de alunos que podem votar: {quantidade_eleitores}")
print(f"Média de idade dos alunos que não podem votar: {media_nao_eleitores:.2f}")
