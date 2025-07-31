n = int(input())
value = list(map(int, input().split()))

min_value = min(value)

ind = value.index(min_value) + 1

print(ind)