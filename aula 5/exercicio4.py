#Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos e quantos são negativos. Determine, também, qual é o menor desses valores. Utilize o comando de repetição que desejar
positivos = 0
negativos = 0
menor = None

print("Digite valores reais (digite 'sair' para encerrar):")

while True:
    entrada = input("Valor: ")

    if entrada.lower() == 'sair':
        break

    try:
        valor = float(entrada)

        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1

    
        if menor is None or valor < menor:
            menor = valor

    except ValueError:
        print("Valor inválido. Digite um número real ou 'sair'.")

print(f"\nQuantidade de valores positivos: {positivos}")
print(f"Quantidade de valores negativos: {negativos}")
if menor is not None:
    print(f"Menor valor digitado: {menor}")
else:
    print("Nenhum valor foi digitado.")
