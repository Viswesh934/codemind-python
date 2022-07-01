def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
x=int(input())
t=int(x)
y=0
y=str(x)
y=y[::-1]
q=int(y)
if (prime(t)==True and prime(q)==True):
    print("circular prime")
elif(prime(t)==True and prime(q)==False):
    print("prime but not a circular prime")
elif(prime(t)==False and prime(q)==False):
    print("not prime")