# cook your dish here
T = int(input())
for i in range(T):
    
    
    x,m,d = map(int,input().split())
    
    
    
    pro = x*m 
    add = x+d
    
    print(min(pro,add))