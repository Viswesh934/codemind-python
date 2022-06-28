t=int(input())
l=list(map(int,input().split()))[:t]
p=[]
for i in l:
    if l.count(i)==i:
        p.append(i)
p=set(p)
print(len(p))