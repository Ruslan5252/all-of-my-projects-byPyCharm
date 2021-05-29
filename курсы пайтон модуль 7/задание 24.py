def summa(*args):
    n = int(input())
    m = int(input())
    a = []
    sum = 0
    for i in range(n):
        row = input().split()
        for j in range(m):
            row[j] = int(row[j])
        a.append(row)

    for i in range(n):
        for j in range(m):
            if i%2==1 and j%2==1:
                sum+=a[i][j]
    print(sum)
    return "КОНЕЦ)"
print(summa())