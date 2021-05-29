import math
print("первый метод sqrt ")
a=int(input("Введите число"))
try:
    print(math.sqrt(a))
except:
    ValueError
    print("функция sqrt дает исключение")
print("второй метод **")
a=int(input("Введите число"))
try:
    print(a**0.5)
except:
    print("Функция ** ворачивает исключение")
print("третий метод pow")
a=int(input("Введите число"))
try:
    print(pow(a,0.5))
except:
    print("функция pow ворачивает исключение")
print("проверка деленя на ноль")
a=int(input("Введите число"))
try:
    print(a/0)
except:
    ZeroDivisionError
    print("деление на ноль")

def example():
    a=[1,2,3,4]
    try:
        print(a[4])
    except:
        print("Вышли за диапазон")
    return "конец функции"
print(example())

t = ('275', '54000', '0.0', '5000.0', '0.0')
try:
    t[0]="20"
    print(t)
except:
    print("кортежи не изменяемые")
    lst = list(t)
    lst[0] = '20'
    t = tuple(lst)
    print(t)