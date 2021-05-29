n = int(input())
m = int(input())
a = []
max=-1
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

for i in range(n):
    for j in range(m):
        if a[j][i]>max:
            max=a[j][i]
    print(max)
    max=0
print()

