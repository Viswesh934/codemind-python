a,b=map(int,input().split())
l=list(map(int,input().split()))[:a]
p=list(map(int,input().split()))[:b]
q=[]
for i in l:
    if i not in p:
        q.append(i)
        
for j in p:
    if j not in l:
        q.append(j)
print(*q)