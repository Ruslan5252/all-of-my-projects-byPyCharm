class Student:
    def __init__(self, name, surname, gpa):
        self.name = name
        self.surname = surname
        self.gpa = gpa

    def getStudentData(self):
        print(f"его имя ", {self.name}, "его фамилее", {self.surname}, "он имеет gpa = ", {self.gpa})


class Main:
    a = []
    while True:
        choice = int(input("PRESS [1] TO ADD STUDENT\nPRESS [2] TO LIST STUDENTS\nPRESS [0] TO EXIT"))
        if choice == 1:
            p = Student(input("Введите его имя"), input("введите фамилию студента"),
                        float(input("введите gpa студента")))
            a.append(p)
        elif choice == 2:
            for i in a:
                i.getStudentData()
        elif choice == 0:
            break