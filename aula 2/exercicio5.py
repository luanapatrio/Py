import math

angulo_graus = float(input("Digite o valor do ângulo em graus: "))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Ângulo em radianos: {angulo_radianos:.4f}")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")