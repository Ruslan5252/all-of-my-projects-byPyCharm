n = int(input())
m = int(input())
a = []

for i in range(n):
    row = input().split()
    for i in range(m):
        row[i] = int(row[i])
    a.append(row)

k = int(input())

for i in range(m):
    print(a[k][i])