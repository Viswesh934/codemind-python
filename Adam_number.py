x=int(input())
y=str(x)
z=int(y[::-1])
z=str(z**2)
if (x**2)==int(z[::-1]):
    print("True")
else:
    print("False")