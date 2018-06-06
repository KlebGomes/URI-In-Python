linha = input().split(" ")

A, B, C = linha
pi = 3.14159

A = float(A)
B = float(B)
C = float(C)

areatriangulo = (A * C)/2
areacirculo = (C * C) * pi
areatrapezio = C * ((A + B)/2)
areaquadrado = B * B
arearetangulo = A * B

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(areatriangulo, areacirculo,areatrapezio, areaquadrado, arearetangulo))
