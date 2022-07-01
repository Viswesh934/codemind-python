n=int(input())
l=n
j=len(str(n))
a=[]
su=0
while n!=0:
    k=n%10
    su=su+k**j
    j=j-1
    n=n//10
if su==l:
    print(True)
else:
    print(False)