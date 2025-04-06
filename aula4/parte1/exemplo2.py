qtdDiarias = int(input("Digite a quantidade de diárias: "))
tipo = input("Digite o tipo de hospedagem: ")

if tipo=="simples" or tipo== "Simples":
    print("Valor a pagar R$ %.2f" %(qtdDiarias * 255.5))
elif tipo=="duplo" or tipo=="Duplo":
    print("Valor a pagar é R$ %.2f" %(qtdDiarias * 305.5))
elif tipo=="triplo" or tipo=="Triplo":
    print("Valor a pagar é R$ %.2f" %(qtdDiarias * 360.5))
else:
    print("Tipo de hospedagem inválida!!")