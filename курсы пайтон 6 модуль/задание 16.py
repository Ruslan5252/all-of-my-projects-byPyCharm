n = int(input())
m = int(input())
a = []
max=0
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

for i in range(n):
    for j in range(m):
        if a[i][j]>max:
            max=a[i][j]
    print(max)

