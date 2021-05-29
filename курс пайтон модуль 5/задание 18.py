"""a = input("введите строку ").split()
a=[i.capitalize() for i in a]
print(a)"""
a = input("введите строку ")
for i in range(len(a)):
    if a[i]==" ":
        a+=a[i+1].upper()
print(a)

