def calcular(h, menor, maior):
    volume = (h/3) * (maior**2 + menor**2 + (maior**2 * menor**2) ** 0.5)
    return volume
    

h = float(input("Digite o valor da altura da pirâmide: "))
menor = float(input("Digite o valor da base menor da pirâmide: "))
maior = float(input("Digite o valor da base maior da pirâmide: "))

volume = calcular(h, menor, maior)

print(f"O volume do tronco da pirâmide é: {volume:.2f}")
