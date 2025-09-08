h, e, a, o, w, x = list(map(int, input().split()))
if w * x > o:
    print('Middle-earth is safe.')
elif w * x <= o:
    print('Sauron has returned')