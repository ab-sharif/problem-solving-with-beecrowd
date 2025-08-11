while True:
    try:
        N = int(input())
        count = 0
        ninjas = 1
        while ninjas < N:
            ninjas *= 2
            count += 1
        print(count)
    except EOFError:
        break