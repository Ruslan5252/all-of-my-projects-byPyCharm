n=int(input("Введите количество элементов массива = "))
b=[]
for i in range(n):
    a=int(input("введите число = "))
    b.append(a)
print(b)
for i in range(n):
    print(b[i]**2)
