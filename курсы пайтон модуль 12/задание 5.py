import os
max=0
min=1000000000
file=open('numbers.txt','r',encoding='utf-8')
x=file.read().split()
for i in x:
    i = int(i)
    if i>max:
        max=i
    if i<min:
        min=i
print(min,max)
file.close()
file2=open('max_min.txt','a')
file2.write(str(min)+"\n")
file2.write(str(max))
