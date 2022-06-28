n=int(input())
l=list(map(int,input().split()))[:n]
b=[]
for i in l:
    if i not in b:
        b.append(i)
s=0
for j in b:
    s+=j
print(s)