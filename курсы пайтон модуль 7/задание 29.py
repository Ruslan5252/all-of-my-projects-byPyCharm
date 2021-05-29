def dva_chisla(*args):
    a=int(input("a="))
    b=int(input("b="))
    if a%2==0 and b%2==0:
        return a*b
    elif a%2==1 and b%2==1:
        return a+b
    elif a%2==1 :
        return a
    elif b%2==1:
        return b
print(dva_chisla())
