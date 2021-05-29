n = int(input())
m = int(input())
a = []
sum = 0
count = 0
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

for i in range(n):
    for j in range(m):
        count += 1
        sum += a[i][j]
        aver = sum / count
        if a[i][j] < aver:
            a[i][j] = 0
    aver = 0
    print(a[i][j], end=" ")
print()
