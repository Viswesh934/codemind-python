t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    p=[]
    for k in range(1,n+1):
        p.append(k)
    for k in p:
        if k not in l:
            print(k)
        
        