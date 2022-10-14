import random
n = int(input("Введите длинну массива: "))
arr=[]
for i in range(n):
    arr.append(random.random() * 100 - 50)
print(arr)
max=arr[0]
count=0
countmax=1
for k in arr:
    count+=1
    if k>max :
        max=k
        countmax=count

print(max)
print(countmax)

for i in range(countmax, n):
        arr[i]=0
print(arr)
        


   
