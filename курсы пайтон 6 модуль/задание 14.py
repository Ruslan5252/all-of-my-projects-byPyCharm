n = int(input())
m = int(input())
a = []
max=0
min=1000000000000
maxi=0
mini=0
maxj=0
maxj=0
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

for i in range(n):
    for j in range(m):
        if a[i][j]>max:
            max=a[i][j]
            maxi=i
            maxj=j
        if a[i][j]<min:
            min=a[i][j]
            mini=i
            minj=j
a[maxi][maxj],a[mini][minj]=a[mini][minj],a[maxi][maxj]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()

