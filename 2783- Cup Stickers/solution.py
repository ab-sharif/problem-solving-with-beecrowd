n, c, m = list(map(int, input().split()))

stampded_cards = list(map(int, input().split()))
bought_cards = list(map(int, input().split()))

missing_count = 0
for card in stampded_cards:
    if card not in bought_cards:
        missing_count += 1

print(missing_count)
