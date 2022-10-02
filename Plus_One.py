n=int(input())
r=list(map(int,input().split()))
s=" "
for i in r:
    i=str(i)
    s+=i
s=int(s)+1
s=list(str(s))
print(*s)
    
