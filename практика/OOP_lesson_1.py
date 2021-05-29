#пример наследования
"""class Person:
    name=1
    age=1
    def set(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    course=1
igor=Student()
igor.set("Игорь",19)
print(igor.name,igor.age)
vlad=Person()
vlad.set("Влад",25)
print(vlad.name+" "+str(vlad.age))"""
#пример полиморфизма
class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def get_area(self):
        return self.a*self.b


class Square:
    def __init__(self,a):
        self.a=a
    def get_area(self):
        return self.a**2


class Circle:
    def __init__(self,r):
        self.r=r
    def get_area(self):
        return 3.14*self.r**2
rect1=Rectangle(12,3)
rect2=Rectangle(5,3)
#print(rect1.get_rect_area())
#print(rect2.get_rect_area())
square1=Square(5)
square2=Square(3)
#print(square1.get_square_area())
#print(square2.get_square_area())
cir1=Circle(5)
cir2=Circle(6)
#print(cir1.get_circle_area())
#print(cir2.get_circle_area())
figures=[rect1,rect2,square1,square2,cir1,cir2]
for figure in figures:
    print(figure.get_area())