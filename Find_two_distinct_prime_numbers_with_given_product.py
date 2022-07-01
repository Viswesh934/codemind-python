def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return False
        else:
            return True
t=int(input())
lis=[]
p=[]
for l in range(t):
    if(prime(t-l)):
        lis.append(t-l)
for i in lis:
    for j in range(len(lis)):
        if i*lis[j]==t:
            p.append(i)
            print(lis[j],end=" ")
if p==[]:
    print(-1)
            

        