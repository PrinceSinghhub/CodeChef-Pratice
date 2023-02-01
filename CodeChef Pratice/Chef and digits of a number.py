t = int(input())
for i in range(t):

    s = input()
    z = 0
    o = 0
    for i in s:
        if i == '0':
            z += 1
        if i == '1':
            o += 1
    if len(s) == 1:
        print('Yes')
    elif min(o, z) == 1:
        print('Yes')
    else:
        print('No')


