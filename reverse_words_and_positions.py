n=input()
s=n.split()
s=s[::-1]
for i in range(len(s)):
    s[i]=s[i][::-1]
print(*s,end=' ')