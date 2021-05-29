a=int(input("координаты ладьи Х>> "))
b=int(input("координаты ладьи Y>> "))
c=int(input("координаты фигуры Х>> "))
d=int(input("координаты фигуры Y>>"))
if a-c==0 or b-d==0:
    print('Yes')
else:
    print("no")