a = input()
str1 = ""
str2 = ""
index  = 1
oper = ""
for i in range(len(a)):
    if a[i].isdigit():
        str1 += a[i]
    else:
        index = i
        oper = a[i]
        break
for i in range(index+1,len(a)):
    if a[i].isdigit():
        str2+=a[i]
    else:
        break
if oper == '+':
    print(int(str1) + int(str2))
if oper =='-':
    print(int(str1) + int(str2))
if oper == '*':
    print(int(str1) + int(str2))
if oper =='/':
    print(int(str1) / int(str2))
