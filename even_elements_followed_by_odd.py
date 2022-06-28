n=int(input())
l=list(map(int,input().split()))[:n]
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
k=e+o
print(*k)