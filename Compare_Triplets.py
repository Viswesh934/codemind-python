r=list(map(int,input().split()))
p=list(map(int,input().split()))
a=0
b=0
c=0
w=[]
for i in range(len(r)):
    if(r[i]>p[i]):
        a+=1
    elif(p[i]>r[i]):
        b+=1
    else:
        c+=1
w.append(a)
w.append(b)
print(*w)