while True:
    try:
        line = input()
        if not line:
            continue

        h, m = map(int, line.split())

        hour = h // 30
        minute = m // 6

        print(f'{hour:02d}:{minute:02d}')

    except EOFError:
        break