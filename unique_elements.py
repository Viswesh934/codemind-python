n=int(input())
l=list(map(int,input().split()))
u=[]
for i in l:
    if i not in u:
        u.append(i)
print(*u)
    