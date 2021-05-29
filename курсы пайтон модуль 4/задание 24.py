n = int(input("Введите количество элементов массива = "))
b = []
sum = 0
count = 0
for i in range(n):
    a = int(input("введите число = "))
    b.append(a)
print(b)
for i in b:
    if i < 0:
        sum += i
        count += 1
aver = sum / count
print(aver)
