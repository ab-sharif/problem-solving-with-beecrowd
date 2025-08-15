total_jeep = 0
total_tourist = 0

while True:
    n = input().strip()

    if n == "ABEND":
        break
    x = n.split()

    action = x[0]
    tourists = int(x[1])

    if action == "SALIDA":
        total_jeep += 1
        total_tourist += tourists
    elif action == "VUELTA":
        total_jeep -= 1
        total_tourist -= tourists

print(total_tourist)
print(total_jeep)