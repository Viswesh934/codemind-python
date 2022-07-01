def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return False
        else:
            return True
t=int(input())
for q in range(t):
    n=int(input())
    for l in range(n):
        if(prime(n-l)):
            print(n-l)
            break
        elif (prime(n+l)):
            print(n+l)
            break