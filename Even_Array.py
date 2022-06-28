t=int(input())
l=list(map(int,input().split()))[:t]
p=[]
for i in l:
    if i%2==0:
        p.append(i)
if len(p)==len(l):
    print("True")
else:
    print("False")
        