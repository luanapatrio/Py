
valor_compra = float(input("Informe o valor da compra: R$ "))


if valor_compra > 200:

    desconto = valor_compra * 0.20
    valor_final = valor_compra - desconto
    print(f"Você recebeu um desconto de R$ {desconto:.2f}. O valor final da compra é: R$ {valor_final:.2f}")
else:
    
    print(f"O valor final da compra é: R$ {valor_compra:.2f}")
