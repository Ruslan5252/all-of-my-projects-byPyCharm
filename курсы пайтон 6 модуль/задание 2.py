n = int(input())
a = []
for i in range(2):
    a.append([int(j) for j in input().split()])
for row in a:
    print(' '.join([str(elem) for elem in row]))