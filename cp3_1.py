name=input("Введите имя: ")
fam=input("Введите фамилию: ")
year=input("Введите год рождения: ")
A=name
B=fam
C=year
D=("")
print(A, end="_")
print(B, end="_")
print(C)
D=A
A=B
B=D
C+=60
print(A, end="_")
print(B, end="_")
print(C)
