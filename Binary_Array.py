def bono(n):
    if n==0 or n==1:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))[:n]
k=[]
for i in l:
    if bono(i):
        k.append(i)
if len(k)==len(l):
    print("True")
else:
    print("False")
    