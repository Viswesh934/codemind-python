s=input()
c=0
for i in range(len(s)):
    if ord(s[i])>=65 or ord(s[i])<=90 or ord(s[i])<=97 or ord(s[i])>=122:
        c+=1
print(c)