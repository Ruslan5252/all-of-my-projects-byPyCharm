class Student:
    def __init__(self,id,name,surname,gpa):
        self.id=id
        self.name=name
        self.surname=surname
        self.gpa=gpa
    def getStudentData(self):
        print(f"id студента = ",{self.id},"его имя ",{self.name},"его фамилее",{self.surname},"он имеет gpa = "
              ,{self.gpa})
    def topStudent(a):
        p=Student(0,"","",0.0)
        for i in a:
            if i.gpa>p.gpa:
                p=i
        p.getStudentData()

class Main:
    a=[]
    i=2
    while i!=0:
        p=Student(input("Введите Id студента"),input("Введите его имя"),input("введите фамилию студента"),
              float(input("введите gpa студента")))
        a.append(p)
        i-=1
    for i in a:
        i.getStudentData()

    def topStudent(a):
        p=Student(0,"","",0.0)
        for i in a:
            if i.gpa>p.gpa:
                p=i
        p.getStudentData()
    topStudent(a)