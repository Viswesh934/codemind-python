def fib(n):
    a=0
    b=1
    c=a+b
    while(c<n):
        c=a+b
        a=b
        b=c
    if(c==n):
        return True
    else:
        return False
n=int(input())
for l in range(n):
    if(fib(n-l) and fib(n+l)):
        print(n-l, n+l)
        break
    elif (fib(n-l)):
        print(n-l)
        break
    elif(fib(n+l)):
        print(n+l)
        break