n = int(input())
speeds = list(map(int, input().split()))

for i in range(1, n):
    if speeds[i] < speeds[i - 1]:
        print(i + 1)
        break

else:
        print(0)