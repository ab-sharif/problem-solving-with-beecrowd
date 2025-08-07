while True:
    n = int(input())
    x = n.count('1')

    if x % 2 == 0:
        print(n + '0')
    else:
        print(n + '1')
