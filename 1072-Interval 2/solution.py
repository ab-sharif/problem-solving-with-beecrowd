in1 = 0
out = 0

for i in range(int(input())):
    n = int(input())
    if n >= 10 and n <= 20:
        in1 += 1
    else:
        out += 1

print(f'''{in1} in
{out} out''')