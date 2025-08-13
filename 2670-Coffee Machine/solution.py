a1 = int(input())
a2 = int(input())
a3 = int(input())

time1 = 0 * a1 + 2 * a2 + 4 * a3

time2 = 2 * a1 + 0 * a2 + 2 * a3

time3 = 4 * a1 + 2 * a2 + 0 * a3

min_time = min(time1, time2, time3)

print(min_time)