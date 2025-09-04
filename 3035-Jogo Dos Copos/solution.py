n = int(input())
pos = input().strip()

for i in range(n):
    move = int(input())

    if move == 1:
        if pos == 'A':
            pos = 'B'
        elif pos == 'B':
            pos = 'A'

    elif move == 2:
        if pos == 'B':
            pos = 'C'
        elif pos == 'C':
            pos = 'B'

    elif  move == 3:
        if pos == 'C':
            pos = 'A'
        elif pos == 'A':
            pos = 'C'

print(pos)