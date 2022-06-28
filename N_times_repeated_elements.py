t=int(input())
l=list(map(int,input().split()))[:t]
k=int(input())
p=[]
for i in l:
    if l.count(i)==k:
        if i not in p:
            p.append(i)

if p==[]:
    print(-1)
else:
    print(*p)