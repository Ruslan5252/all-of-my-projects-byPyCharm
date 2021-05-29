n=int(input("введите первое число "))
m=int(input("введите второе число "))
count=0
for i in range(n,m+1):
    if i%2==0:
        count+=1
print(count)