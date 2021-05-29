def calculate(*args):
    a=int(input("Введите число 1 "))
    b=int(input("Введите число 2 "))
    c=input("Введите оператор ")
    if c=='+':
        return f"a+b={a+b}"
    elif c=="-":
        return f"a-b={a-b}"
    elif c=="*":
        return f"a*b={a*b}"
    elif c=="/":
        return f"a/b={a/b}"
print(calculate())