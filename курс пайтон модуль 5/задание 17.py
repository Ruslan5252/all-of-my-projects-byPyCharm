str = input()
str2=''
for i in str:
    if i.isupper():
        i=i.lower()
        str2+=i
    elif i.islower():
        i=i.upper()
        str2+=i
    elif i==' ':
        str2+=' '
print(str2)


