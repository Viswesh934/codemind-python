n=int(input())
l=list(map(int,input().split()))
c=[]
d=0
for i in l:
    i=str(i)
    c.append(int(i[::-1]))
print(*c)