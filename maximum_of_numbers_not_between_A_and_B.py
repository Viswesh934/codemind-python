n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
p=[]
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        p.append(l[i])
if len(p)==0:
    print(-1)
else:
    print(max(p))
        