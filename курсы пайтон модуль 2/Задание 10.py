a=int(input("Введите первое число "))
b=int(input("Введите второе число "))
c=int(input("Введите третье число "))
d=int(input("Введите четвертое число "))
if a>c and a>b and a>d and a%2==0:
    print(a)
elif b>a and b>c and b>d and a%2==0:
    print(b)
elif c>a and c>b and c>d and a%2==0:
    print(c)
elif d>a and d>b and d>c and a%2==0:
    print(d)
else:
    print('Not Found')