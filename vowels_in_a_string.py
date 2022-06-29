string =input()
n=input()
c=0
vowels = "AEIOUaeiou"
for i in range(len(string)):
    if string[i]==n:
        c+=1
        break
if c==0:
    print("False")
else:
    print("True")
    print(i)
        