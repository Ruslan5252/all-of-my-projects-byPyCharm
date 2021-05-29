
def arifm(n, b=[]):
    count=0
    sum=0
    for i in range(n):
        a = int(input("Введите элемент матрицы "))
        b.append(a)
    for i in range(n):
        if b[i]%2==0:
            count+=1
            sum+=b[i]
    aver=sum/count
    print("среднее значение = ", aver)
    return "конец функции"
print(arifm(6))