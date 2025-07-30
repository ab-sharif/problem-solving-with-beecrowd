while True:
    n = int(input())

    if n == 0:
        break

    matrix = []

    for r in range(n):
        row = []
        for c in range(n):
            row.append(0)
        matrix.append(row)

    for r in range(n):
        for c in range(n):
            matrix[r][c] = 2 ** (r + c)

    t = len(str(matrix[n-1][n-1]))

    for i in range(n):
        for j in range(n):
            matrix[i][j] = str(matrix[i][j])
            while len(matrix[i][j]) < t:
                matrix[i][j] = ' ' + matrix[i][j]
        m = ' '.join(matrix[i])
        print(m)

    print()
