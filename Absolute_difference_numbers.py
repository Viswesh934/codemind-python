a,b=map(int,input().split())
i=str(a)
j=int(i[ :b])
k=len(i)-b
l=int(i[k: ])
if j>l:
    print(j-l)
else:
    print(l-j)