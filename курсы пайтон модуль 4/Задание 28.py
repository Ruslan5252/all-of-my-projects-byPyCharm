n = int(input("Введите число= "))
b = []
c = []
while n != 0:
    b.append(n)
    n = int(input("Введите число= "))
print(b)
for i in b:
    if i > 0:
        c.append(i)
print(c)
