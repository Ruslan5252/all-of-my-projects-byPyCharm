n=int(input("Введите количество элементов массива = "))
b=[]
count=0
for i in range(n):
    a = int(input("введите число = "))
    if a>0:
        b.append(a)
        count += 1
print(b)
print("количество положительных элементов",count)