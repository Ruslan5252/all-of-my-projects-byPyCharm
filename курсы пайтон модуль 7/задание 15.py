def dvum_matr(n,a=[]):
    for i in range(n):
        row = input().split()
        for j in range(n):
            row[j] = int(row[j])
        a.append(row)
    a[0], a[n - 1] = a[n - 1], a[0]
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()
    return "КОНЕЦ)"
print(dvum_matr(4))


"""n = int(input())

a = []
for i in range(n):
    row = input().split()
    for j in range(n):
        row[j] = int(row[j])
    a.append(row)
a[0],a[n-1]=a[n-1],a[0]
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()"""