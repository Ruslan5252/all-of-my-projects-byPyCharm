n=int(input("введите первое число "))
sum=0
k=1
for i in range(1,n+1):
    if k%2==1:
        sum += k
        k+=2
print(sum)
