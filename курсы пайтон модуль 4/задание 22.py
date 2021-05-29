n = int(input())
mass = list()
max = -1
min = 10000000
index1 = 0
index2 = 0
for i in range(n):
    numbers = int(input())
    mass.append(numbers)
for i in range(n):
    if mass[i] > max:
        max = mass[i]
        index1 = i
    if mass[i] < min:
        min = mass[i]
        index2 = i
mass[index2],mass[index1] = mass[index1],mass[index2]
print(mass)


