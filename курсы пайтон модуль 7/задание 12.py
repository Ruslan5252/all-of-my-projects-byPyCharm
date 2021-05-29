
def max_and_min(n, b=[]):
    max = 0
    min = 10000000
    for i in range(n):
        a = int(input("Введите элемент матрицы "))
        b.append(a)
    for i in range(n):
        if b[i] > max:
            max=b[i]
        if b[i] < min:
            min=b[i]
    print("max = ",max)
    print("min = ",min)
    return "конец функции"
print(max_and_min(6))

