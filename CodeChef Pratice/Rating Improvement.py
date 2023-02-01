t = int(input())

for i in range(t):
    
    X,Y = map(int,input().split())
    
    solRating = Y  
    Y = X+200
    
    if solRating in range(X,Y+1):
        print('YES')
    
    else:
        print('NO')
    
    