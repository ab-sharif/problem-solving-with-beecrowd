n = int(input())

for i in range(n):
    name, nmbr = input().split()
    nmbr = int(nmbr)

    if name == "Thor":
        print('Y')
    else:
        print('N')
