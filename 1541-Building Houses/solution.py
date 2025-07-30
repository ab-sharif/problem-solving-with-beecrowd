while True:
    x = input().split()

    if "0" in x:
        break

    A, B, C = map(int, x)
    h_a = A * B
    y = C / 100
    l_a = h_a / y
    l = int(l_a ** 0.5)
    print(l)