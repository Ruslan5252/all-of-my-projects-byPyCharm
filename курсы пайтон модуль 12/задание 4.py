import os
file=open('info.txt','r',encoding='utf-8')
filedata=file.read().lower()
filedata=filedata.replace('my','your')
fout=open("info.txt",'w')
fout.write(filedata)
fout.close()
file.close()