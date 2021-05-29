a = input("text")
print(a[::-1])
for i in range(len(a)):
    print(a[len(a)-i-1],end="")