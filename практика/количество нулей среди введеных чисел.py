n=int(input("введите количество чисел "))
count=0
for i in range(1,n+1):
    a=int(input("Введите числа "))
    if a==0:
        count+=1
print(f"количество нулей среди {n} чисел =  ",count)
