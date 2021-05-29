import random
a=[]
b=[]
c=[]
for i in range(10):
    d=random.randint(1,100)
    a.append(d)
print(a)
for i in range(10):
    e=random.randint(1,100)
    b.append(e)
print(b)
for i in range(10):
    c.append(a[i]+b[i])
print(c)