B = int(input())
G = int(input())

x = G // 2

if x <= B:
    print('Amelia tem todas bolinhas!')
elif x > B:
    print(f'Faltam {x - B} bolinha(s)')