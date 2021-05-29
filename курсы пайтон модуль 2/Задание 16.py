a=int(input("Введите первое число "))
b=int(input("Введите второе число "))
c=int(input("Введите третье число "))
if a>10 and b>10 and c>10 and a%5==0 and b%5==0 and c%5==0:
    print("yes")
else:
    print("no")