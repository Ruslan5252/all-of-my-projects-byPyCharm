def matrix(*args):
    b=[]
    n=int(input("Введите количество элементов массива "))
    m=int(input("Введите число m "))
    for i in range(n):
        a=int(input("Введите элементв массива "))
        b.append(a)
    for i in range(n):
        if i==b[i] and b[i]%m!=0:
            print(b[i])
    return "END"
print(matrix())
