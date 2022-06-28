n=int(input())
l=list(map(int,input().split()))[:n]
l.extend(l)
c=0
for i in range(0,len(l)-1):
    if l[i+1]%2==0 and l[i-1]%2!=0:
        c+=1
    elif l[i-1]%2!=0 and l[i+1]%2==0:
        c+=1
        
print(c)