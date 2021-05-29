def massiv(*args):
    n=int(input('Введите количество элементов массива '))
    b=[]
    for i in range(n):
        a = int(input("Введите элемент матрицы "))
        b.append(a)
    for i in range(n):
        if b[i]<50 and b[i]%5==0:
            print(b[i])
    return "Конец"
print(massiv())