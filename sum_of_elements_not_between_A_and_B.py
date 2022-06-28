n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
c=0
m=[ ]
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        c+=l[i]
        m.append(l[i])
print(c)