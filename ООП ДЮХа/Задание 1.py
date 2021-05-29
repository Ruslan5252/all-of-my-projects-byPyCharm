class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def getData(self):
        print(f"Длина = {self.a}\nШирина = {self.b}\nПериметр = {self.perimetr()}\nПлощадь = {self.square()}")


a = Rectangle(2, 3)
a.perimetr()
a.square()
a.getData()
