def isprime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
            break
    else:
        return True
n=int(input())
t=0
for i in range(2,n):
    for j in range(2,n):
        if (isprime(i) and isprime(j)):
            r=i*j
            if r==n and i<j:
                print(i,j)
                t=1
                break
if t==0:
    print(-1)
        