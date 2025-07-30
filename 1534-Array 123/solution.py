while True:
    try:

        N = int(input())

        if 3 <= N <= 70:

            matrix = []

            for r in range(N):
                row = []
                for c in range(N):
                    row.append(3)
                matrix.append(row)

            # print(matrix)

            for r in range(N):
                matrix[r][r] = 1
                matrix[r][N - r - 1] = 2

            for r in range(N):
                for c in range(N):
                    print(matrix[r][c], end="")
                print()

    except EOFError:
        break