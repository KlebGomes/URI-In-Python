from math import sqrt
p1 = input().split(' ')
p2 = input().split(' ')

x1, y1 = p1
x2, y2 = p2

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

dis = sqrt(((x2 - x1) ** 2) + ((y2 - y1)**2))

print('{:.4f}'.format(dis))
'''
import math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1,y1 = linha1
x2,y2 = linha2

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

res = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("{:.4f}".format(res))
'''