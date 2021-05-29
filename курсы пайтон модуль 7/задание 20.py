def sezon(*args):
    n=int(input("Введите номер месяца "))
    if n==1 or n==2 or n==12:
        print("Winter")
    if 3<=n<=5:
        print("Spring")
    if 6<=n<=8:
        print("Summer")
    if 9<=n<=11:
        print("Autumn")
    return "конец функции"
print(sezon())