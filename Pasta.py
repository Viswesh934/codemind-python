from re import A


n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(m):
    flag = 1
    for j in range(n):
        if b[i] == a[j]:
            a[j] = -1
            flag = 0
            break
    if flag:
        print("No")
        exit()
print("Yes")
