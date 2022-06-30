n=int(input())
l=list(map(int,input().split()))[:n]
s=0
for i in range(len(l)):
    s+=l[i]
print(s)