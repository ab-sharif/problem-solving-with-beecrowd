n = int(input())

for i in range(n):
    b = int(input())

    ai, di, li = map(int, input().split())
    ai2, di2, li2 = map(int, input().split())

    l1 = (ai + di) / 2
    l2 = (ai2 + di2) / 2

    if li % 2 == 0:
        l1 += b

    if li2 % 2 == 0:
        l2 += b

    if l1 > l2:
        print('Dabriel')
    elif l2 > l1:
        print('Guarte')
    else:
        print('Empate')