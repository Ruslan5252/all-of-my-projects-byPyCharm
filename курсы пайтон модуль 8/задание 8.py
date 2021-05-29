class User():
    def __init__(self,id,login,password,name,surname):
        self.id=id
        self.login=login
        self.password=password
        self.name=name
        self.surname=surname
    def getData(self):
        print(f"Id ",{self.id},"login",{self.login},"password ",{self.password},
              "имя",{self.name},"фамилие ",{self.surname})
class Staff(User):
    def __init__(self,id,login,password,name,surname,salary):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.salary=salary
    def getData(self):
        print(f"Id ", {self.id}, "login", {self.login}, "password ", {self.password},
              "имя", {self.name}, "фамилие ", {self.surname},'зарпалата',{self.salary})
    def addSubject(self,subject=[]):
        self.subject=subject
        p=Staff(input("Введите id"),input("Введите login"),input("Введите password"),input("Введите name"),
                input("Введите фамилее"),input("Введите salary "))
        subject.append(p)
class Student(User):
    def __init__(self,id,login,password,name,surname,gpa):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.gpa=gpa
    def getData(self):
        print(f"Id ", {self.id}, "login", {self.login}, "password ", {self.password},
                "имя", {self.name}, "фамилие ", {self.surname},"gpa",{self.gpa})
    def addCourse(self,course=[]):
        self.course=course
        a=Student(input("Введите id"),input("Введите login"),input("Введите password"),input("Введите name"),
                input("Введите фамилее"),input("Введите gpa "))
        course.append(a)
class Main():
    b=[]
    i=5
    while i!=0:
        p = Staff(input("Введите id"), input("Введите login"), input("Введите password"), input("Введите name"),
                  input("Введите фамилее"), input("Введите salary "))
        a = Student(input("Введите id"), input("Введите login"), input("Введите password"), input("Введите name"),
                    input("Введите фамилее"), input("Введите gpa "))
        b.append(p)
        b.append(a)
        i-=1
    for i in b:
        i.getData()

