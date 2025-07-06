pn = 0
avg = 0

for i in range(6):
    n = float(input())
    if n > 0:
        pn += 1
        avg += n

print(f'''{pn} valores positivos
{(avg / pn):.1f}''')