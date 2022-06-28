n=int(input())
l=list(map(int,input().split()))[:n]
p=(sum(l)//len(l))
if p in l:
    print("True")
else:
    print("False")