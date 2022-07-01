def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
a=[]
n=int(input())
for i in range(0,n):
    print(fib(i),end=" ")