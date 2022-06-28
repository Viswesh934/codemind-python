n=int(input())
l=list(map(int,input().split()))[:n]
p=int(input())

if p in l:
    print("True")
else:
    print("False")