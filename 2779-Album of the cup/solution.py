import sys

data = sys.stdin.read().split()

nums = list(map(int, data))

N = nums[0]
M = nums[1]

stickers = nums[2:]

unique_stickers = set(stickers)

missing = N - len(unique_stickers)

print(missing)
