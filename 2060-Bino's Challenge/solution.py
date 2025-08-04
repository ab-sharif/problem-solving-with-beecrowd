n= int(input())
number = map(int, input().split())

x2 = x3 = x4 = x5 = 0

for i in number:
    if i % 2 == 0:
        x2 += 1
    if i % 3 == 0:
        x3 += 1
    if i % 4 == 0:
        x4 += 1
    if i % 5 == 0:
        x5 += 1

print(f'{x2} Multiplo(s) de 2')
print(f'{x3} Multiplo(s) de 3')
print(f'{x4} Multiplo(s) de 4')
print(f'{x5} Multiplo(s) de 5')