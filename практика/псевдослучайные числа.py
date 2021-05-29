import random

group0 = 0
group10 = 0
group20 = 0
group30 = 0
group40 = 0
group50 = 0
group60 = 0
group70 = 0
group80 = 0
group90 = 0
i=0
while i != 100000:
    a = random.randint(0, 99)
    if 0 < a < 9:
        group0 += 1
    if 10 < a < 19:
        group10 += 1
    if 20 < a < 29:
        group20 += 1
    if 30 < a < 39:
        group30 += 1
    if 40 < a < 49:
        group40 += 1
    if 50 < a < 59:
        group50 += 1
    if 60 < a < 69:
        group60 += 1
    if 70 < a < 79:
        group70 += 1
    if 80 < a < 89:
        group80 += 1
    if 90 < a < 99:
        group90 += 1
    i += 1
print(sum)
print(group0)
print(group10)
print(group20)
print(group30)
print(group40)
print(group50)
print(group60)
print(group70)
print(group80)
print(group90)
