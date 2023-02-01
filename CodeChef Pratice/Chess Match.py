# cook your dish here
n = int(input())

for i in range(n):
    N, A, B = map(int, input().split())

    ans = 2 * (180 + N) - (A + B)

    print(ans)