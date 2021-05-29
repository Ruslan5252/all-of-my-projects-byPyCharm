n=int(input("Введите количество элементов массива = "))
b=[]
for i in range(n):
    a=int(input("введите число = "))
    b.append(a)
b.sort(reverse=True)
print(b)