n = int(input())
for i in range(n):
    h, m, o = map(int, input().split())

    time_str = f"{h:02d}:{m:02d}"

    if o == 1:
        status = "A porta abriu!"
    else:
        status = "A porta fechou!"

    print(f'{time_str} - {status}')