a=int(input("Введите первое число "))
b=int(input("Введите второе число "))
c=int(input("Введите третье число "))
if a>b and a>c:
    if(b+c)>a:
        print("yes")
    else:
        print("no")
elif b>a and b>c:
    if(a+c)>b:
        print("yes")
    else:
        print("no")
elif c>a and c>b:
    if(b+a)>c:
        print("yes")
    else:
        print("no")

