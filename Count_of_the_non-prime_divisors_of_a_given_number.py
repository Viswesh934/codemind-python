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
c=0
d=[]
for i in range(1,n+1):
    if isprime(i)==False:
        if n%i==0:
            c+=1
print(c)