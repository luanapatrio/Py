idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Classe eleitoral: Não-eleitor")
elif 18 <= idade <= 65:
    print("Classe eleitoral: Eleitor obrigatório")
else:
    print("Classe eleitoral: Eleitor facultativo")
