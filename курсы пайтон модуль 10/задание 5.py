class User():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def getdata(self):
        print(self.name, self.surname, self.age)


class Main:
    arr = []
    i = 2
    count = 0
    sum = 0
    while i != 0:
        name = input("Введите имя")
        surname = input("Введите фамилию")
        age = input("Введите возраст")
        try:
            Person = User(name, surname, int(age))
        except :
            Person = User(name, surname, 0)
        arr.append(Person)
        i -= 1
    for i in arr:
        i.getdata()
    for i in arr:
        count += 1
        sum += i.age
    aver = sum / count
    print(aver)
