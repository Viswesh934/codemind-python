def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return False
        else:
            return True
m=[]
n=int(input())
for l in range(n):
    if(prime(n-l)):
        m.append(n-l)
        break
for l in range(n):
    if (prime(n+l)):
        m.append(n+l)
        break
k=[]
k.append(abs(n-m[0]))
k.append(abs(n-m[1]))
print(min(k))