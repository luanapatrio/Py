import math

# Solicita os coeficientes ao usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula o discriminante (Delta)
delta = b**2 - 4*a*c

# Calcula as raízes usando a fórmula de Bhaskara
raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)

# Exibe os resultados
print(f"As raízes da equação são: {raiz1:.2f} e {raiz2:.2f}")


#Feito pelo Chatgpt pois não entendi como utilizar as fórmulas, necessito tirar dúvidas na aula.
