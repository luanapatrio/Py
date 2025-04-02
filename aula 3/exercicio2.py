#Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de
#horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a
#seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um
#caractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$
#37,50


turno = input("Informe seu turno de trabalho: ").upper()
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))

if turno == 'N':
    valor_hora = 45.00
else:
    valor_hora = 37.50

salario = horas_trabalhadas * valor_hora

print(f"Seu salário é: R$ {salario:.2f}")
