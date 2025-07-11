max_number = 0
position = 0

for i in range(1, 100):
    n = int(input())
    if n > max_number:
        max_number = n
        position = i

print(f'{max_number}')
print(f'{position}')