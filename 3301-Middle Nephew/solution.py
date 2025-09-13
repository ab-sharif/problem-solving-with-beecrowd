while True:
    try:
        H, Z, L = map(int, input().split())

        ages = [(H, 'huguinho'), (Z, 'zezinho'), (L, 'luisinho')]

        ages.sort()

        print(ages[1][1])

    except EOFError:
        break