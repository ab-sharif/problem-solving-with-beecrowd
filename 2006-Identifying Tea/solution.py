n = int(input())

a, b, c, d, e = map(int, input().split())

count = 0

if a == n:
    count += 1
if b == n:
    count += 1
if c == n:
    count += 1
if d == n:
    count += 1
if e == n:
    count += 1

print(count)