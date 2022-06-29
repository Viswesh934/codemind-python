n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
c=0
m=max(l)
for i in l:
    i=str(i)
    m=str(m)
    if len(i)==len(m):
        c+=1
print(c)
        