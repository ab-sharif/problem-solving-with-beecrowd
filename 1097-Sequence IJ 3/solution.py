k = 7
for i in range(10):
    if i % 2 != 0:
        for j in range(3):
            j = k - j
            print(f'I={i} J={j}')

        k += 2