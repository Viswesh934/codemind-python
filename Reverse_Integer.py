n=int(input())
w=n
if(n<0):
    n=-1*n
re=0
while (n> 0):  
    r=n% 10
    re= (re* 10) + r
    n= n // 10  
if(w>0):
    print(re)
if(w<0):
    print(-1*re)