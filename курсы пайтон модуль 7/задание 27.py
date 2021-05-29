def spisok(*args):
    b=[]
    n=int(input("Введите количество элементов "))
    max=0
    min=1000000000
    indexmax=0
    indexmin=0
    for i in range(n):
        a=int(input("Введите количество элементов массива "))
        b.append(a)
    for i in range(n):
        if b[i]>max:
            max=b[i]
            indexmax=i
        if b[i]<min:
            min=b[i]
            indexmin=i
    b[indexmax]=min
    b[indexmin]=max
    print(b)
    return "END"
print(spisok())