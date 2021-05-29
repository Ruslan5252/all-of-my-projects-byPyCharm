n=int(input("Введите количество элементов массива = "))
b=[]
sum=0
for i in range(n):
    a = int(input("введите число = "))
    sum+=a
    b.append(a)
print(b)
print("сумма всех элементов массива ",sum)