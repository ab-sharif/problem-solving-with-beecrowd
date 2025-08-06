import math

n = int(input())

sqrt_5 = math.sqrt(5)
x = (1 + sqrt_5) / 2
y = (1 - sqrt_5) / 2

result = (x ** n - y ** n) / sqrt_5

print(f'{result:.1f}')