import os
f=open('students.txt','r',encoding='utf-8')
count=0
for x in f:
    count+=1
print("Количество строк = ", count)