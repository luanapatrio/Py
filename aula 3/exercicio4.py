
conta_agua = float(input("Informe o valor da conta de água: R$ "))
conta_luz = float(input("Informe o valor da conta de luz: R$ "))
conta_telefone = float(input("Informe o valor da conta de telefone: R$ "))
salario = float(input("Informe o valor do seu salário: R$ "))

total_contas = conta_agua + conta_luz + conta_telefone

if salario < total_contas:
    print("Salário insuficiente!")
else:
    salario_restante = salario - total_contas
    print(f"Após pagar as contas, o valor restante do seu salário é: R$ {salario_restante:.2f}")
