n=int(input())
l=list(map(int,input().split()))
p=l[:n//2]
k=l[n//2:]
print(abs(sum(p)-sum(k)))
    