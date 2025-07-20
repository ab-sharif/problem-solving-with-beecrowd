age = []

while True:
    n = int(input())
    if n < 0:
        break
    else:
        age.append(n)

result = sum(age) / len(age)
print(f'{result:.2f}')