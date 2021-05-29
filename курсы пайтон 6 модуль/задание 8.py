n = int(input())
m = int(input())
a = []

for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

for i in range(n):
    for j in range(m):
            print(a[i][j]**2,end=" ")
    print('\n')
