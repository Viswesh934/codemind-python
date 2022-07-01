t=int(input())
def gcd(a,b):
    if a>b:
        a,b=b,a
    for i in range(1,b+1,1):
        if a%i==0 and b%i==0:
            c=i
    return c          
a=list(map(int,input().split()))
agcd=gcd(a[0],a[1])
for i in range(2,len(a)):
    agcd=gcd(agcd,a[i])
print(agcd)
