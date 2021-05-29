def dvum_matr(n,a=[]):
    for i in range(n):
        row = input().split()
        for j in range(n):
            row[j] = int(row[j])
        a.append(row)
    for i in range(n):
        for j in range(n):
            if i==j:
                print(a[i][j], end=" ")
        print()
    return "КОНЕЦ)"
print(dvum_matr(3))