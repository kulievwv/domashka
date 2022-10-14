import math
a=float(input("Введите первый катет: "))
b=float(input("Введите второй катет: "))

c=float(math.sqrt(a*a+b*b))
S=(a*b)/2
P=a+b+c
print("Площадь: ", S)
print("Периметр: ",P)
