n=int(input())
l=list(map(int,input().split()))[:n]
p=max(l)
b=[]
c=0
for i in l:
    if l.count(i)==i:
        b.append(i)
for i in l:
    if l.count(i)!=i:
        c+=1
if c==n:
    print(-1)
else:
    print(min(b),max(b))
        
        