import random
def razryad(*args):
    b=[]
    a=random.randint(1000,9999)
    a1 = a % 10
    print(a1, "единицы ")
    a2 = a // 10
    a3 = a2 % 10
    print(a3, "десятка")
    a4 = a // 100
    a5 = a4 % 10
    a6 = a // 1000
    print(a5, "сотни")
    print(a6, "тысячи")
    return "END"
print(razryad())
