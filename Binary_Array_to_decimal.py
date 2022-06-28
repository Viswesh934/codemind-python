n=int(input())
l=list(map(int,input().split()))[:n]
l=l[::-1]
d=0
for i in range(0,len(l)):
    d+=(l[i]*pow(2,i))
print(d)
