a,b=map(int,input().split())
if(a > b):
    maximum = a
else:
    maximum = b

while(True):
    if(maximum % a == 0 and maximum % b == 0):
        print( maximum)
        break;
    maximum = maximum + 1