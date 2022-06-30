def isprime(num):

	if num==1:
	    return False
	for i in range(2,int(num**0.5)+1):
	    if num%i==0:
	        return False
	        break
	else:
	    return True
m=int(input())
n=int(input())
c=0
d=[]
for i in range(m,n+1):
    if isprime(i):
        c+=1
print(c)
    