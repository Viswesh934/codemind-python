p,r,t=map(int,input().split())
d=pow(1+r/100,t)
print("%0.2f"%(p*d))