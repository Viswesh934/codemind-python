n=int(input())
l=list(map(int,input().split()))[:n]
c=[]
d=[]
for i in l:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
    
print(*(d+c))