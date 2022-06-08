def f():
   n = int(input())
   pl = [int(x) for x in input().split()]
   nepar = []
   for i in pl:
      if i % 2 == 1:
         nepar.append(i)
   if len(nepar) > 1:
      return len(nepar) // 2
   return 0
t = int(input())
for i in range(t):
   print(f())#wierd palindrome making