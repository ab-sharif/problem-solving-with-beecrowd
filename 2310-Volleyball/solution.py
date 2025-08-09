n = int(input())

total_service = total_block = total_attack = 0
success_service = success_block = success_attack = 0

for i in range(n):
    name = input()
    a, b, c = map(int, input().split())
    a1, b1, c1 = map(int, input().split())

    total_service += a
    total_block += b
    total_attack += c

    success_service += a1
    success_block += b1
    success_attack += c1

service_percent = (success_service / total_service) * 100
block_percent = (success_block / total_block) * 100
attack_percent = (success_attack / total_attack) * 100

print(f'Pontos de Saque: {service_percent:.2f} %.')
print(f'Pontos de Bloqueio: {block_percent:.2f} %.')
print(f'Pontos de Ataque: {attack_percent:.2f} %.')
