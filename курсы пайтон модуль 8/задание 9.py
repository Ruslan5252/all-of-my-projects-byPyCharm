class Car():
    def __init__(self,name,model,maxSpeed,year,volume):
        self.name=name
        self.model=model
        self.maxSpeed=maxSpeed
        self.year=year
        self.volume=volume
    def ride(self):
        print(f"машина названием ",{self.name},"моделью ",{self.model},"с максимальной скоростью ",{self.maxSpeed},
              "с годом выпуска ",{self.year},"с объемом",{self.volume},'is riding')
class Toyota(Car):
    def __init__(self,name,model,maxSpeed,year,volume,manufacturer):
        self.name=name
        self.model=model
        self.maxSpeed=maxSpeed
        self.year=year
        self.volume=volume
        self.manufcturer=manufacturer
    def ride(self):
        print(f"машина с названием ",{self.name},"моделью ",{self.model},"с максимальной скоростью ",{self.maxSpeed},
              "с годом выпуска ",{self.year},"с объемом",{self.volume},
              'произведенная в ',{self.manufcturer},'is riding')
class Mercedes(Car):
    def __init__(self,name,model,maxSpeed,year,volume,class_Type):
        self.name=name
        self.model=model
        self.maxSpeed=maxSpeed
        self.year=year
        self.volume=volume
        self.class_Type=class_Type
    def ride(self):
        print(f"машина с названием ", {self.name}, "моделью ", {self.model}, "с максимальной скоростью ", {self.maxSpeed},
              "с годом выпуска ", {self.year}, "с объемом", {self.volume},
              'имеющая  ', {self.class_Type},'класс is riding')
class Main():
    b=[]
    i=3
    while i!=0:
        c=Car(input("Введите название машины "), input("Введите модель"), input("Введите максимальную скорость "),
                   input("введите год выпуска машины "),
                  input("Введите объем машины "))
        p = Toyota(input("Введите название машины  "), input("Введите модель"), input("Введите максимальную скорость "),
                   input("введите год выпуска машины "),
                  input("Введите объем машины "), input("Введите страну производства "))
        a = Mercedes(input("Введите название машины "), input("Введите модель"), input("Введите максимальную скорость "),
                   input("введите год выпуска машины "),
                  input("Введите объем машины "), input("введите класс машины  "))
        b.append(p)
        b.append(a)
        b.append(c)
        i-=1
    for i in b:
        i.ride()