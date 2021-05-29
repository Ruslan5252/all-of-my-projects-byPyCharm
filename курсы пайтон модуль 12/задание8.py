class User():
    def __init__(self,id,login,password):
        self.id=id
        self.login=login
        self.password=password
    def toString(self):
        print(self.id,self.login,self.password)
class Main(User):
    def getUsersList():
        file = open("memory.txt", "r")
        x=file.read().split()
        print(x,end="\n")
    def saveUsers(self):
        file=open("memory.txt",'a')
        file.write('id '+self.id+'\n')
        file.write('login '+self.login+'\n')
        file.write('password '+self.password+'\n'+'\n')
    while True:
        choice = int(input("PRESS [1] TO ADD User\nPRESS [2] TO LIST User\nPRESS [0] TO EXIT\n"))
        if choice==1:
            file = open("memory.txt", 'a')
            p = User(input("Введите Id"), input("введите login"),
                        (input("введите password")))
            saveUsers(p)
        elif choice==2:
            file = open("memory.txt", "r")
            getUsersList()
        elif choice==0:
            break
