n=int(input("Введите целое число"))
if n>=1 and n<=5:
    n=n+10
    print(n)
elif 10<=n<=20:
    n=n-5
    print(n)
elif n<0 or n>1000:
    n=n*3
    print(n)
else:
    n=0
    print(n)

