n=int(input("Введите количество элементов массива = "))
b=[]
sum=0
max_elem=0
p=1
for i in range(n):
    a = int(input("введите число = "))
    sum+=a
    b.append(a)
print(b)
for i in range(n):
    if b[i]==0:
        continue
    p *= b[i]
print(p)