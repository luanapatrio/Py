
salario_fixo = float(input("Digite o salário fixo do funcionário: R$ "))
valor_vendas = float(input("Digite o valor total das vendas: R$ "))


comissao = valor_vendas * 0.04
salario_final = salario_fixo + comissao


print(f"\nComissão: R$ {comissao:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
