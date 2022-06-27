def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
c1=0
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
for i in a:
    if not prime(i):
        c1+=1
print(c1)
        