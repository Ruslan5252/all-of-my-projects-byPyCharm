a=input("Первое число")
b=input("Второе число")
try:
    ans=int(a)+int(b)
except:
    ans=str(a)+str(b)
print(ans)
