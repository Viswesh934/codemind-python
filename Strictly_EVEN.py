n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(len(l)):
    if l[i]%2==0:
        if i%2!=0:
            print("False")
            break
else:
    print("True")