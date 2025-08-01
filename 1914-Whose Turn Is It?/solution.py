n = int(input())

for i in range(n):
    name1, x, name2, y = input().split()

    a, b = map(int, input().split())

    total = a + b

    if total % 2 == 0:
        if x == 'PAR':
            print(name1)
        else:
            print(name2)
    else:
        if x == 'IMPAR':
            print(name1)
        else:
            print(name2)