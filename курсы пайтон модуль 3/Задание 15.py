n=int(input("введите первое число "))
m=int(input("введите второе число "))
s=0
for i in range(n,m+1):
    if i%2==0:
        s+=i
print(s)