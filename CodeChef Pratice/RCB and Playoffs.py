T = int(input())

for i in range(T):
    X,Y,Z = map(int,input().split())
    
    if Y-X > Z*2:
        print("No")
        
    else:
        print("Yes")