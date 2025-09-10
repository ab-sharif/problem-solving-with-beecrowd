t = int(input())

for _ in range(t):
    parts = list(map(int, input().split()))
    k = parts[0]
    strips = parts[1:]



    total_outlets = sum(strips)
    usable = total_outlets - (k - 1)

    print(usable)