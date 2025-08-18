x = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

n = list(map(int, input().split()))

total_x = sum(x)

winner_index = (total_x - 1) % 9

print(x[winner_index])