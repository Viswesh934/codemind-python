n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
m=[]
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        print(l[i],end=' ')
        m.append(l[i])
if len(m)==0:
    print(-1)
