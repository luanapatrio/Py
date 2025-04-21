nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


if 9.0 <= media <= 10.0:
    conceito = "A"
    situacao = "APROVADO"
elif 7.5 <= media < 9.0:
    conceito = "B"
    situacao = "APROVADO"
elif 6.0 <= media < 7.5:
    conceito = "C"
    situacao = "APROVADO"
elif 4.0 <= media < 6.0:
    conceito = "D"
    situacao = "REPROVADO"
else: 
    conceito = "E"
    situacao = "REPROVADO"

print(f"\nMédia: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")
