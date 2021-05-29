def matrix(*args):
    b=[]
    max=0
    min=10000000000
    n=int(input("Введите количество элементов массива "))
    for i in range(n):
        a=int(input("Введите элементв массива "))
        b.append(a)
    for i in range(n):
        if b[i]>max:
            max=b[i]
        if b[i]<min:
            min=b[i]
    summa=max+min
    print(summa)
    return "END"
print(matrix())
