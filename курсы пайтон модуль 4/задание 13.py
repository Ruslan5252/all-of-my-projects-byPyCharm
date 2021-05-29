n=int(input("Введите количество элементов массива = "))
b=[]
for i in range(n):
    a = int(input("введите число = "))
    if a>0:
        b.append(a)
print(b)