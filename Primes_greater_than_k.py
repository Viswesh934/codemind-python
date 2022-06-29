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
k=int(input())
s=[]
for i in l:
    if isprime(i):
        s.append(i)
c=0
for i in s:
    if i>=k:
        c+=1
print(c)