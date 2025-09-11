e, f, c = map(int, input().split())
total_bottles = e + f
drand = 0

while total_bottles >= c:
    new_sodas = total_bottles // c
    drand += new_sodas
    total_bottles = new_sodas + (total_bottles % c)

print(drand)