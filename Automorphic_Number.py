x=int(input())
y=x**2
k=str(y)
l1=len(str(x))
if str(x)==k[-l1:]:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")