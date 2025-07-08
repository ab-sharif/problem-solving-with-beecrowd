n = int(input())
odd = []

while True:
    if n % 2 == 1:
        print(n)
        odd.append(n)
        if len(odd) == 6:
            break
    n += 1