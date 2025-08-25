import sys

lines = sys.stdin.read().splitlines()
i = 0

while i < len(lines):
    x, y, m = map(int, lines[i].split())
    i += 1

    for _ in range(m):
        xi, yi = map(int, lines[i].split())
        i += 1

        if (xi <= x and yi <= y) or (yi <= x and xi <= y):
            print('Sim')
        else:
            print('Nao')
