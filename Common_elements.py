a,b=map(int,input().split())
l=list(map(int,input().split()))[:a]
p=list(map(int,input().split()))[:b]
c=[]
d=[]
for i in l:
    if i in p:
        c.append(i)
for j in c:
    if j not in d:
        d.append(j)
print(*d)