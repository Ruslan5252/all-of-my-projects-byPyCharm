def massiv(*args):
    n=int(input('Введите количество элементов массива '))
    b=[]
    for i in range(n):
        a = int(input("Введите элемент матрицы "))
        b.append(a)
    for i in range(n):
        if b[i]%2==1:
            print(b[i])
        if b[i+1]==23:
            break
    return "END"
print(massiv())