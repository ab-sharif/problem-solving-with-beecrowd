while True:
    try:
        names = [input().strip() for _ in range(10)]
        print(names[2])  # 3rd name (index 2)
        print(names[6])  # 7th name (index 6)
        print(names[8])  # 9th name (index 8)
    except EOFError:
        break