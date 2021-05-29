def spisok(*args):
    b=[]
    n=int(input("Введите количество элементов "))
    sum=0
    for i in range(n):
        a=int(input("Введите элемент "))
        b.append(a)
    for i in range(n):
        if b[i]%2==0 and b[i]<11:
            sum+=b[i]
    print(sum)
    return "END"
print(spisok())