N=int(input())
r=list(map(int,input().split()))
c=0
p=0
for i in r:
    if i%2==0:
        c+=1
    else:
        p+=1
print(c,end=" ")
print(p)