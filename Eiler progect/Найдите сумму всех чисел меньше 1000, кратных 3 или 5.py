# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
scetchik = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        scetchik += i
print(scetchik)



