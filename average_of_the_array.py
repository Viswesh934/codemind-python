n=int(input())
l=list(map(int,input().split()))[:n]
print("%0.2f"%(sum(l)/len(l)))
