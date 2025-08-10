try:
    while True:
        letter = input()
        n = int(input())
        number = list(map(int, input().split()))

        message = ''
        for i in number:
            message += letter[i-1]

        print(message)

except EOFError:
    pass