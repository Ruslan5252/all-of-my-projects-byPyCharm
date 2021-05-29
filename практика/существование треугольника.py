def trugolnik(*args):
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    if a+b>c or b+c>a or c+a>b:
        return "Yes"
    else:
        return "No"
print(trugolnik())