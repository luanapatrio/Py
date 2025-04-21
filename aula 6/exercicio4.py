segundos_totais = int(input("Digite a quantidade de segundos: "))


horas = segundos_totais // 3600
segundos_restantes = segundos_totais % 3600

minutos = segundos_restantes // 60
segundos = segundos_restantes % 60


print(f"\nResultado:")
print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
