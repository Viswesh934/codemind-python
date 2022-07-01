h=int(input())
j=int(input())
def sum(n):
    k=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            k=k+i
    return k
k1=sum(h)
k2=sum(j)
if k1==j and k2==h:
    print("Amicable")
else:
    print("Not Amicable")