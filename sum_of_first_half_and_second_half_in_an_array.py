n=int(input())
l=list(map(int,input().split()))[:n]
s=l[:n//2]
p=l[n//2:]
print(sum(s))
print(sum(p))