n=int(input("Введите количество элементов массива = "))
arr=[]
index1 = 0
index2 = 0
sum = 0
for i in range(n):
    a=int(input("Введите число = "))
    arr.append(a)

for i in range(n):
    if arr[i] == 0:
        index1 = i
        break

for i in range(n):
    if arr[n-i-1] == 0:
        index2 = n-i-1
        break

for i in range(index1,index2+1):
    sum += arr[i]

print(sum)
