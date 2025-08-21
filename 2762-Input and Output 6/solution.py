while True:
    try:
        number = input()
        if "." in number:
            left, right = number.split('.')
            print(f'{int(right)}.{left}')
    except EOFError:
        break