def sd(a,b):
    def d(n):
        for i in str(n):
            if i=='0' or n%int(i)>0:
                return 0
        return 1
    m=[]
    for i in range(a,b+1):
        if d(i)==1:
            m.append(i)
    return m
        
a=int(input())
b=int(input())
j=sd(a,b)
k=list(filter(None,j))
for i in k:
    print(i,end=" ")