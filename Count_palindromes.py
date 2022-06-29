n=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    i=str(i)
    if i==i[::-1]:
        c+=1
print(c)