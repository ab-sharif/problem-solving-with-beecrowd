while True:
    try:
        n, my_id = map(int, input().split())
        count = 0

        for _ in range(n):
            author_id, game_type = map(int, input().split())
            if author_id == my_id and game_type == 0:
                count += 1

        print(count)

    except EOFError:
        break