string =input()
vowels = "aeiou"
vowels=list(vowels)
r=[]
for i in string:
    if i in vowels:
        if i not in r:
            r.append(i)
if len(r)==len(vowels):
    print("True")
else:
    print("False")