n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    i=str(i)
    if int(i)<0:
        i=abs(int(i))
    if len(str(i))==k:
        c+=1
print(c)