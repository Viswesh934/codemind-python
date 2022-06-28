n=int(input())
l=list(map(int,input().split()))[:n]
b=[]
for i in l:
    if i not in b:
        b.append(i)
su=0
for i in b:
    if i%2!=0:
        su+=i
print(su)