altura = float(input("Digite sua altura em metros (ex: 1.75): "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44
else:
    print("Sexo inválido informado.")
    peso_ideal = None

if peso_ideal is not None:
    print(f"\nSeu peso ideal é: {peso_ideal:.2f} kg")
