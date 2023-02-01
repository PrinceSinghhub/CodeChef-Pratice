t = int(input())
for i in range(t):

    W, X, Y, Z = map(int, input().split())

    water = W + Y * Z

    if water == X:
        print('filled')

    elif water < X:
        print('unfilled')

    else:
        print('overflow')