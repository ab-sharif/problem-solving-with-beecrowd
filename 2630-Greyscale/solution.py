n = int(input())
count = 0
for i in range(n):
    x = input()
    count += 1
    r, g, b = map(int, input().split())

    if x == "eye":
        p = (0.30 * r) + (0.59 * g) + (0.11 * b)
    elif x == "max":
        p = max(r, g, b)
    elif x == "min":
        p = min(r, g, b)
    else:
        p = (r + g + b) / 3

    print(f'Caso #{count}: {int(p)}')