t = int(input())
for i in range(t):

    n = int(input())
    todo = list(map(int, input().split()))

    count = 0

    for i in todo:
        if i > 999:
            count += 1
    print(count)