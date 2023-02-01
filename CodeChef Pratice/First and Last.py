t = int(input())

for i in range(t):
    
    N = int(input())
    
    arr = list(map(int,input().split()))
    
    if len(arr) < 3:
        print(sum(arr))
    
    
    else:
        
        
        Max = arr[0] + arr[-1]
        
        for i in range(N-1):
            
            if Max < arr[i] + arr[i+1]:
                Max = arr[i] + arr[i+1]
        
        print(Max)
        
        
