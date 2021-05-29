n=int(input("Введите количество элементов массива = "))
b=[]
sum=0
count=0
for i in range(n):
    a = int(input("введите число = "))
    sum+=a
    count+=1
    b.append(a)
print(b)
print(sum)
print(sum/count)