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
m=int(input())
for i in range(n,m+1):
    if prime(i):
        print(i)