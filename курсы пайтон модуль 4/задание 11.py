n=int(input("Введите количество элементов массива = "))
b=[]
for i in range(n):
    a = int(input("введите число = "))
    if i%2==1:
        b.append(a)
print(b)