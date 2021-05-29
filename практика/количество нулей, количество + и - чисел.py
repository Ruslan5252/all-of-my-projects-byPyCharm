n=int(input("введите количество чисел "))
count_null=0
count_negative=0
count_positive=0
for i in range(1,n+1):
    a=int(input("Введите числа "))
    if a==0:
        count_null+=1
    elif a<0:
        count_negative+=1
    elif a>0:
        count_positive+=1
print(f"количество нулей среди {n} чисел = {count_null}")
print(f"количество отрицательных чисел среди {n} чисел = {count_negative}")
print(f"количество положительных чисел среди {n} чисел = {count_positive} ")
