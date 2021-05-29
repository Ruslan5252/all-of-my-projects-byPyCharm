class Phone:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def getData(self):
        print(f"Name: {self.name}, Model: {self.model}, Price: {self.price}")
i=5
a=[]
while i!=0:
    p = Phone(input("Введите название телефона "),input("введите модель "), input("введите цену "))
    p.getData()
    i-=1
