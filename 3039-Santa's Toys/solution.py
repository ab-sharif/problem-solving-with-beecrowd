x = int(input())
girl = 0
boy = 0

for i in range(x):
    name, count = input().split()
    if count == "F":
        girl += 1
    elif count == "M":
        boy += 1

print(f'{boy} carrinhos')
print(f'{girl} bonecas')