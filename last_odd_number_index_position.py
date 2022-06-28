n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(1,len(l)):
    if l[i]%2!=0:
        po=i
print(po)
        