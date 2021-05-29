n = int(input("Введите количество элементов массива = "))
b = []
m = ""
for i in range(n):
    a = int(input("введите число = "))
    b.append(a)
print(b)
m = int(input("введите число для поиска"))
if m in b:
    print("Yes", f"индекс введенного числа {i}")
else:
    print("No")
