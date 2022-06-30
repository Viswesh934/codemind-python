n=int(input())
p=n*n
s=0
for i in range(n):
    r=p%10
    s+=r
    p=p//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")