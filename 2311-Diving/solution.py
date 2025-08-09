n = int(input())

for i in range(n):
    name = input()
    difficulty = float(input())
    scores = list(map(float, input().split()))

    scores.remove(max(scores))
    scores.remove(min(scores))

    result = sum(scores) * difficulty

    print(f'{name} {result:.2f}')

