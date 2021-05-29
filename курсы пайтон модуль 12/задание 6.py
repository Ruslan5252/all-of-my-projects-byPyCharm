import os
file=open("numbers.txt","r")
x=file.read().split()
for i in range(len(x)):
    x[i]=int(x[i])
x.sort()
print(x)
file.close()
file1=open("numbers.txt",'a')
for i in x:
    file1.write(str(i)+'\n')

