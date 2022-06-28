n=int(input())
l=list(map(int,input().split()))[:n]
k=0
p=0
for i in range(len(l)):
    if l[i]%2==0:
        k+=l[i]
    else:
        p+=l[i]
print(k)