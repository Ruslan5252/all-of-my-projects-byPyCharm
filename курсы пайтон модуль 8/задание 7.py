class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printData(self):
        print(f"имя ",{self.name},"его возраст ",{self.age}," его зарпалата = ",{self.salary})
class Programmer(Employee):
    def __init__(self,name,age,salary,programminLanguage):
        self.name = name
        self.age = age
        self.salary = salary
        self.programminLanguage=programminLanguage
    def printData(self):
        print(f"имя ",{self.name},"его возраст ",{self.age}," его зарпалата = ",{self.salary},
              "язык на котором он пишет",{self.programminLanguage})
class DataAnalitics(Employee):
    def __init__(self,name,age,salary,databaseTool):
        self.name = name
        self.age = age
        self.salary = salary
        self.databaseTool=databaseTool
    def printData(self):
        print(f"имя ",{self.name},"его возраст ",{self.age}," его зарпалата = ",{self.salary},
              {self.databaseTool})
class Main:
    a=[]
    p = Programmer(input("имя "), input("возраст"), input("зарплата "),input("язык на котором он пишет"))
    d = DataAnalitics(input("имя "), input("возраст"), input("зарплата "),input("databaseTool"))
    a.append(p)
    a.append(d)
    p.printData()
    d.printData()
