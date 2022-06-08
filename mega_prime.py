N=int(input())
d=0
pd=0
for i in range(2,(N//2)+1):
    if N%i==0:
        print("Not Mega Prime")
        break
else:
    while N:
        r=N%10
        d+=1
        if r==2 or r==3 or r==5 or r==7:
            pd+=1
        N=N//10
    if d==pd:
            print("Mega Prime")
    else:
           print("Not Mega Prime")