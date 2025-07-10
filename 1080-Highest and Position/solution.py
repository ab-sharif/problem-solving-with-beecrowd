max_value = 0
position = 0

for i in range(1, 101):
    n = int(input())
    if n > max_value:
        max_value = n
        position = i

print(f'''{max_value}
{position}''')