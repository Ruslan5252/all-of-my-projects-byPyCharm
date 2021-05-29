def massiv(n):
    b = []
    ans = []
    a = input("Введите элемент ").split()
    for i in range(n):
        b.append(a[i])

    for i in range(len(b)):
        flag = True
        for j in range(len(b)):
            if b[i] == b[j] and i != j:
                flag = False
        if flag == True:
            ans.append(b[i])

    return ans
n = int(input())
print(massiv(n))