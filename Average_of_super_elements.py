n =int(input())
a=list(map(int,input().split()))[:n]
b=[]
for i in a:
    if a.count(i)==i:
        if i not in b:
            b.append(i)
if b==[]:
    print(-1)
else:
    print("%0.2f"%(sum(b)/len(b)))
        