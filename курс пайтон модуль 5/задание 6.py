a = input()
b = input()
flag = True
index = 0
for i in range(len(a)):
    if a[i] == b:
        flag =False
        index = i
if flag==True:
    print("THERE IS NO SUCH LETTER")
else:
    print(index)