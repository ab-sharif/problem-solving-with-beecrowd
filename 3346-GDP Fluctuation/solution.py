F1, F2 = map(float, input().split())

gdp_after_first_year = 1 + (F1 / 100)

gdp_after_second_year = gdp_after_first_year * (1 + (F2 / 100))

total_change = (gdp_after_second_year - 1) * 100

print(f"{total_change:.6f}")
