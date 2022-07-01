n=int(input())
s=0
a=[]
for i in range(1,n//2+1):
    if n%i==0:
        a.append(i)
for i in a:
    s=s+i
if s>n:
    print(True)
else:
    print(False)