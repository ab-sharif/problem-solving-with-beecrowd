while True:
    try:
        line = input().strip()
        dd, mm, yy = line.split('/')

        print(f"{mm}/{dd}/{yy}")
        print(f"{yy}/{mm}/{dd}")
        print(f"{dd}-{mm}-{yy}")

    except EOFError:
        break  