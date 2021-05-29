n = int(input("Введите количество элементов\n"))
mass = []
for i in range(n):
    key = input("Введите синонимы -").split()
    mass.append(key)
d = dict(mass)
word = input("Введите ключ\n")
print(d.get(word))