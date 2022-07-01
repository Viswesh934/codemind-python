n=input()
s=list(n)
if len(set(s))==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")