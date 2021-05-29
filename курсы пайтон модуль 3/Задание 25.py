a = 1
p = 1
while a != 0:
    a = float(input("введите дробное число"))
    if a==0:
        break
    p *= a
    print(p)

print("конечный ответ",round(p,2))
