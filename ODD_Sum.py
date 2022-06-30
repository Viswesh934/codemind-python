n=int(input())
l=list(map(int,input().split()))[:n]
s=0
for i in range(len(l)):
    if l[i]%2!=0:
        s+=l[i]
print(s)