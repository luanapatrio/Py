produto = input("Digite o nome do produto: ")
valor_compra = float(input("Digite o valor de compra do produto: R$ "))

if valor_compra < 10:
    valor_venda = valor_compra * 1.70
elif 10 <= valor_compra < 30:
    valor_venda = valor_compra * 1.50
elif 30 <= valor_compra < 50:
    valor_venda = valor_compra * 1.40
else:
    valor_venda = valor_compra * 1.30

print(f"\nProduto: {produto}")
print(f"Valor da venda: R$ {valor_venda:.2f}")
