def isprime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
            break
    else:
        return True
n=int(input())
l=list(map(int,input().split()))[:n]
c=0
for i in l:
    if isprime(i):
        c+=1
print(c)