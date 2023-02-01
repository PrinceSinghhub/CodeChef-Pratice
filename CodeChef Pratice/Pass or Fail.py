# cook your dish here


n = int(input())
for i in range(n):
    N, X, P = map(int, input().split())

    wq = N - X
    obtainMarks = X * 3

    ans = obtainMarks - wq

    if ans >= P:
        print("Pass")
    else:
        print("Fail")

