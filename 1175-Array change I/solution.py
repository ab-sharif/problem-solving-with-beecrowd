a = []

for i in range(5):
    n = int(input())
    a.append(n)

count = 0
for j in a[::-1]:
    print(f'N[{count}] = {j}')
    count += 1