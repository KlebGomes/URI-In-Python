linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, qtd1, prec1 = linha1
cod2, qtd2, prec2 = linha2

total = (int(qtd1) * float(prec1)) + (int(qtd2) * float(prec2))

print('VALOR A PAGAR: R$ %0.2f' %total)
