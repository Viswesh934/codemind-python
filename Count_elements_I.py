a,b=map(int,input().split())
l=list(map(int,input().split()))[:a]
p=list(map(int,input().split()))[:b]
l=set(l)
p=set(p)
c=0
for i in l:
    if i in p:
        c+=1
print(c)