n=int(input("Введите количество элементов массива = "))
b=[]
for i in range(n):
    a=int(input("введите элемент "))
    b.append(a)
print(b)

for i in range(n):
    print(i,b[i])

