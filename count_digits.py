n=int(input())
l=list(map(int,input().split()))
p=[]

for i in l:
    i=str(i)
    if int(i)<0:
        i=str(abs(int(i)))
    p.append(len(i))
print(*p)
    
    
        