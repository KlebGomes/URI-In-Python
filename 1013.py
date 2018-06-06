valores = input().split(' ')

a, b, c = valores

MaiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2
resultado = (int(MaiorAB) + int(c) + abs(int(MaiorAB) - int(c))) / 2

print('{} é o maior.'.format(resultado))
