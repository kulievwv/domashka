import random
n1 = int(input("Введите длину массива A: "))
n2 = int(input("Введите длину массива B: "))
A=[]
B=[]
C=[]
D=[]
for i in range(n1):
    A.append(round(random.random() * 10 - 5))
for i in range(n2):
    B.append(round(random.random() * 10 - 5))    
print(A)
print(B)
b=0
for i in range(1, n1):
    for j in range(1, n2):
             if A[i]==B[j]:
                    C.append(A[i])
                    b+=1
if b>0:
    for i in C:
       if i not in D:
         D.append(i)
    print("Общие элементы:")
    print(D)    
     
else:
    print("Совпадений нет.")
