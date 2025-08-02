n = int(input())

max_number = -1
register_max = -1

for i in range(n):
    reg, number = input().split()
    number = float(number)
    reg = int(reg)

    if number > max_number:
        max_number = number
        register_max = reg

if max_number >= 8.0:
    print(register_max)
else:
    print('Minimum note not reached')
