d1 = int(input().split()[-1])
h1, m1, s1 = map(int, input().split(" : "))

d2 = int(input().split()[-1])
h2, m2, s2 = map(int, input().split(" : "))

t1 = (d1 * 24 * 60 * 60) + (h1 * 60 * 60) + (m1 * 60) + s1
t2 = (d2 * 24 * 60 * 60) + (h2 * 60 * 60) + (m2 * 60) + s2

d = h = m = s = 0
for i in range(t1, t2):
    s += 1
    if s == 60:
        m += 1
        s = 0
        if m == 60:
            h += 1
            m = 0
            if h == 24:
                d += 1
                h = 0

print(f'''{d} dia(s)
{h} hora(s)
{m} minuto(s)
{s} segundo(s)''')