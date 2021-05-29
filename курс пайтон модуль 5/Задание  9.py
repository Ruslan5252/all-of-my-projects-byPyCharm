a = input("text")
b = input("word")
b==b.lower()
count=0
for i in a.lower():
    if i==b:
        count+=1
print(count)