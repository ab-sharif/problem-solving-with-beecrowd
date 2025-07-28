mode = input()
matrix = []
n = 12

for r in range(n):
    row = []
    for items in range(n):
        item = float(input())
        row.append(item)

    matrix.append(row)

output = 0
no_item = 0
for i in range(n):
    item_select = matrix[i][n-i:]
    output += sum(item_select)
    no_item += len(item_select)

if mode == 'S':
    print(f'{output:.1f}')

if mode == 'M':
    output = output / no_item
    print(f'{output:.1f}')