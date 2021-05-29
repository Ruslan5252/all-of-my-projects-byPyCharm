n = int(input("Введите количество элементов массива = "))
b = []
m=""
sum = 0
count = 0
for i in range(n):
    a = int(input("введите число = "))
    b.append(a)
print(b)
m=int(input("введите число m = "))
for i in b:
    if i>m:
        count+=1
        sum+=i
aver=sum/count
print(aver)