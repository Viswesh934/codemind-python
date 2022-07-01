
x=int(input())
c=0
for i in range(1,x+1):
    if i*(i+1)==x:
        c=1
if c==1:
    print("YES")
elif c==0:
    print("NO")