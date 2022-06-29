string =input()
vowels = "aeiou"
vowels=list(vowels)
r=[]
for i in string:
    if i in vowels:
        vowels.remove(i)
if vowels==[]:
    print(0)
else:
    print(*vowels,end=" ")