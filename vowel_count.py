string =input()
vowels = "AEIOUaeiou"
vowels=list(vowels)
r=[]
c=0
for i in string:
    if i in vowels:
        c+=1
if c==0:
    print(0)
else:
    print(c)
