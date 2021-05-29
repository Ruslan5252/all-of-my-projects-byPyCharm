x=int(input("x= "))
s=""
while x!=0:
    s=s+str(x%10)
    x=x//10
print(s)
