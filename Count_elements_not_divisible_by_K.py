n,k=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i%k!=0:
        c.append(i)
print(len(c))
    