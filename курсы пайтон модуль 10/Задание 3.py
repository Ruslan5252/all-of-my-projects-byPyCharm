a=[]
while True:
    b = int(input("Введите число"))
    if b==0:
        break
    a.append(b)
print(a)
c=int(input("Введите целое число в качестве индекса"))
try:
    print(a[c])
except:
    print("Нет такого элемента в списке")


