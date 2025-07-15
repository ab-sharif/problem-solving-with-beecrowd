alcohol = 0
gasoline = 0
disel = 0

while True:
    n = int(input())
    if n == 1:
        alcohol += 1

    if n == 2:
        gasoline += 1

    if n == 3:
        disel += 1

    if n == 4:
        break

print('MUITO OBRIGADO')
print(f'Alcood: {alcohol}')
print(f'Gasolina: {gasoline}')
print(f'Diesel: {disel}')