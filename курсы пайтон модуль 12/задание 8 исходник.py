import os
"""def saveUsers(id,log,passw):
    file=open("mem.txt",'a')
    if id==' ' or log==' ' or passw==' ':
        return "Пропущено одно или несколько полей ввода"
    else:
        file.write('id '+str(id)+'\n')
        file.write('login '+str(log)+'\n')
        file.write('password '+str(passw)+'\n'+'\n')
        file.close()
saveUsers(input("id "),input("login "),input("password "))


def getUsersList():
    file = open("mem.txt", "r")
    x = file.read().split()
    print(x, end="\n")
getUsersList()

"""

file=open("mem.txt",'r')
file.read(1)