while True:
    try:
        t = int(input())
        time = []
        for i in range(t):
            time.append(float(input()))
        print(min(time))
    except EOFError:
        break