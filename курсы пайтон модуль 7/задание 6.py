def glasn(str=''):
    count = 0
    str=str.lower()
    for i in str.lower():
        if i == 'a' or i == "e" or i=='i' or i=='o' or i=="u":
            count +=1
    return count
print(glasn("google"))



