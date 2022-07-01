def pal(n):
    k=str(n)
    if n==int(k[::-1]):
        return True
    else:
        return False
t=int(input())
for i in range(t):
    a=int(input())
    print(pal(a))