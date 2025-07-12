n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    if x > y:
        x, y = y, x

    list = []

    for j in range(x+1, y):
        if (j % 2) != 0:
            list.append(j)

    total = sum(list)
    print(total)