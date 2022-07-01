n=input()
p=input()
n=(n.lower()).split()
p=(p.lower()).split()
c=[]
r=" "
for i in p:
    if i in n:
        c.append(i)
        print(i,end=" ")

        
