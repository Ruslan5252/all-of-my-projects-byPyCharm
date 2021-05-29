def massiv(*args):
    n=int(input("Введите количество элементов в массиве "))
    b=[]
    sum=0
    for i in range(n):
        a=int(input("Введите элемент массива "))
        b.append(a)
    for i in range(n):
        if b[i]%5==0:
            continue
        else:
            sum+=b[i]
    return sum
print(massiv())