n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    while i!=0:
        r=i%10
        c+=r
        i=i//10
print(c)
    