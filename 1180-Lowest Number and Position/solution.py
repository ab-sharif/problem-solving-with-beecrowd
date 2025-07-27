n = int(input())
list_x = list(map(int, input().split()))

x = list_x[:n]

min_val = min(x)
index_min_val = x.index(min_val)

print(f'Menor valor: {min_val}')
print(f'Posicao: {index_min_val}')