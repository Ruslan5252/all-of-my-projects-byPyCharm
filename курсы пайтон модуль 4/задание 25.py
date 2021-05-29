n = int(input("Введите количество элементов массива = "))
b = []
sum = 0
count = 0
for i in range(n):
    a = int(input("введите число = "))
    b.append(a)
print(b)
for i in b:
    sum += i
    count += 1
aver = sum / count
print(aver)
for i in b:
    if i>aver:
        print(i)