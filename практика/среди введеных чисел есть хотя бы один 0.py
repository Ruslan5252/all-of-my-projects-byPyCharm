n=int(input("введите количество чисел "))
for i in range(1,n+1):
    a=int(input("Введите числа "))
    if a==0:
        print("Yes")
        break
    elif a!=0:
        print("No")