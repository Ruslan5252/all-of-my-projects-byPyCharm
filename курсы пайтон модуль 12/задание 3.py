import os
f=open('students.txt','r',encoding='utf-8')
max_len=''
for x in f:
    if len(x)>len(max_len):
        max_len=x
print(len(max_len),max_len,end=' ')
