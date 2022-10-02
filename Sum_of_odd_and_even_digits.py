n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    if i%2==0:
        o+=l[i]
    else:
        e+=l[i]

if(e-o==0):
    print("YES")
else:
    print("NO")