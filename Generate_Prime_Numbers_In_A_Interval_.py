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
m=int(input())
for i in range(n,m+1):
    if isprime(i):
        print(i)