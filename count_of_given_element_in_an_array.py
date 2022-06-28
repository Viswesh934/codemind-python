n=int(input())
l=list(map(int,input().split()))[:n]
p=int(input())
c=0
for i in range(len(l)):
    if p==l[i]:
        c+=1
print(c)