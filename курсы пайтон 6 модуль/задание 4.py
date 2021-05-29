n = int(input())
m = int(input())
a = []

for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)


for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print(a[i][j],end=" ")