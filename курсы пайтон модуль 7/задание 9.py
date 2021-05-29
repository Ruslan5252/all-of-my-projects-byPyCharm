def massiv(n,b=[]):
    count=0
    for i in range(n):
        a=int(input("Введите элемент "))
        b.append(a)
        if b[i]==0:
            count+=1
    return count
print(massiv(6))