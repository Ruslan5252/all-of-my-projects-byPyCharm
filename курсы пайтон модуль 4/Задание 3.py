x = list()
y = int(input('Введите количество элементов - '))
for i in range(y):
    z = int(input())
    x.append(z)
arr = tuple(x)
flag = True
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        flag = False
        break
if flag == True:
    print('EQUAL')
else:
     print('NOT EQUAL')
