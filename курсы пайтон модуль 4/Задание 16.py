n=int(input("Введите количество элементов массива = "))
b=[]
sum=0
max_elem=0
for i in range(n):
    a = int(input("введите число = "))
    sum+=a
    b.append(a)
print(b)

for i in range(n):
    if b[i]>max_elem:
        max_elem=b[i]
print(f"максимальный элемент массива = {max_elem}, а его индекс = {i}")