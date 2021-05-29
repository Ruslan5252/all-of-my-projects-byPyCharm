n=int(input("Введите количество элементов массива = "))
b=[]
sum=0
max_elem=0
min_elem=1000000
count=0
for i in range(n):
    a = int(input("введите число = "))
    b.append(a)
print(b)
for i in range(n):
    if b[i]>max_elem:
        max_elem=b[i]
    if b[i]<min_elem:
        min_elem=b[i]
b.remove(max_elem)
b.remove(min_elem)
print(b)
for i in b:
    sum+=i
    count+=1
    aver=sum/count
print(sum,aver)



