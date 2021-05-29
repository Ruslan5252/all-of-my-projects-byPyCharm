a=input("Введите номер телефона с целыми числами")
try:
    print(int(a))
except:
    ValueError
    print("Вы ввели неверный формат")