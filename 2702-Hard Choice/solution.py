ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

if cr > ca:
    missed_chicken = cr - ca
else:
    missed_chicken = 0

if br > ba:
    missed_beef = br - ba
else:
    missed_beef = 0

if pr > pa:
    missed_pasta = pr - pa
else:
    missed_pasta = 0

total = missed_chicken + missed_beef + missed_pasta
print(total)