songs = [
    "PROXYCITY",
    "P.Y.N.G.",
    "DNSUEY!",
    "SERVERS",
    "HOST!",
    "CRIPTONIZE",
    "OFFLINE DAY",
    "SALT",
    "ANSWER!",
    "RAR?",
    "WIFI ANTENNAS"
]

C = int(input())

for _ in range(C):
    x, y = map(int, input().split())
    print(songs[x + y])