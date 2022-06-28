t=int(input())
l=list(map(int,input().split()))[:t]
p=[]
for i in l:
    if l.count(i)==i:
        if i not in p:
            p.append(i)
c=0
for i in p:
    if p.count(i)!=i:
        c+=1
if p==[]:
    print(-1)
else:
    print(*p)