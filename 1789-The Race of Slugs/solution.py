while True:
    try:
        l = int(input())
        speeds = list(map(int, input().split()))

        m_speed = max(speeds)

        if m_speed < 10:
            print(1)
        elif 10 <= m_speed < 20:
            print(2)
        else:
            print(3)

    except EOFError:
        break