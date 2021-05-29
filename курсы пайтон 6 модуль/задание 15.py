n = int(input())
m = int(input())
a = []
k=int(input("введите К "))
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    a.append(row)

for i in range(n):
    for j in range(m):
        if a[i][j]%k==0:
            ostatok=a[i][j]/k
            a[i][j]=int(ostatok)
        print(a[i][j],end=" ")
    print()

