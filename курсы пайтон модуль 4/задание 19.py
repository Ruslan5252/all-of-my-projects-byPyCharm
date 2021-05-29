n=int(input("Введите количество элементов массива = "))
b=[]
sum=0
max_elem=0
min_elem=1000000
for i in range(n):
    a = int(input("введите число = "))
    b.append(a)
print(b)

for i in range(n):
    if b[i]>max_elem:
        max_elem=b[i]
    if b[i]<min_elem:
        min_elem=b[i]
print(f"максимальный элемент массива = {max_elem}, а минимальный элемент = {min_elem}")