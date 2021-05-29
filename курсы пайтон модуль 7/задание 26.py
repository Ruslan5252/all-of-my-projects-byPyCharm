def spisok(*args):
    b=[]
    n=int(input("Введите количество элементов "))
    m=int(input("Введите число m "))
    count=0
    sum=0
    for i in range(n):
        a=int(input("Элемент массива "))
        b.append(a)
    for i in range(n):
        count+=1
        sum+=b[i]
        aver=sum/count
    print(aver)
    for i in range(n):
        if b[i]>m:
            b[i]=aver
    return b
print(spisok())

