anos = float(input("Digite sua idade em anos:"))
meses = float(input("Digite os meses adicionais:"))
dias= float(input("Digite os dias adicionais:"))

apenas_dias = (anos * 365) + (meses * 30) + dias

print(f"Sua idade expressa em dias é: {apenas_dias} dias.")