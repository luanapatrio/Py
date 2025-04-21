import math
area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))


litros_necessarios = area / 3

latas_necessarias = math.ceil(litros_necessarios / 18)

preco_total = latas_necessarias * 80


print(f"\nVocê precisará comprar {latas_necessarias} lata(s) de tinta.")
print(f"Preço total: R$ {preco_total:.2f}")
