prestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite o valor da multa: "))
dias = float(input("Digite os dias em atraso:"))

valor = prestacao + (prestacao * (multa/100) * dias)

print(f"O valor da prestação com o atraso agora é de: {valor:.2f}")