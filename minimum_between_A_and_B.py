n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
p=[]
for i in l:
    if i>=a and i<=b:
        p.append(i)
if p==[]:
    print(-1)
else:
    print(min(p))