n = int(input("Введите количество элементов массива = "))
b = []
m=""
sum = 0
count = 0
for i in range(n):
    a = int(input("введите число = "))
    b.append(a)
print(b)
for i in b:
    if i%2==0 or i==0:
        count+=1
        sum+=i
aver=sum/count
print(aver)