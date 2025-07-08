p = n = o = e = 0

for i in range(5):
    m = int(input())
    if m > 0:
        p += 1
    elif m < 0:
        n += 1

    if m % 2 == 0:
        e += 1
    else:
        o += 1

print(f'''{e} valor(es) par(es)
{o} valor(es) impar(es)
{p} valor(es) positivo(s)
{n} valor(es) negativo(s)''')