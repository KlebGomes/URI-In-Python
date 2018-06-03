funcionario = input()
salfixo = float(input())
vendas = float(input())

salario = float(salfixo + (vendas * (15/100)))

print('TOTAL = R$ %0.2f' %salario)