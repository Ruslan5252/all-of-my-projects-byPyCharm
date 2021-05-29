class Phone:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def getData(self):
        print(f"Name: {self.name}, Model: {self.model}, Price: {self.price}")


p = Phone("iPhone", "iPhone 11", 50000)
p.getData()
