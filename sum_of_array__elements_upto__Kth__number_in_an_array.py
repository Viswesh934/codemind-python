n=int(input())
l=list(map(int,input().split()))[:n]
p=int(input())
s=0
for i in range(len(l)):
    if i==p:
        break
    else:
        s+=l[i]
print(s)