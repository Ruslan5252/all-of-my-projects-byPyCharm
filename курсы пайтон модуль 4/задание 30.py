n=int(input("Введите количество элементов массива = "))
b=[]
sum=0
for i in range(n):
    a = int(input("введите число = "))
    b.append(a)
k=int(input("Введите К = "))
for i in b:
    if i%k==0 and i!=0:
        print(i)
