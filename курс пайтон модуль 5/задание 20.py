a = input("длинный текст ").split()
b = input("слово которое хотите поменять")
c = input("слово на которое хотите поменять")
for i in range(len(a)):
    if a[i] == b:
        a[i] = c
print(a)
