def iHN(num):    
    rem = sum = 0   
    while(num > 0):    
        rem = num%10 
        sum = sum + (rem*rem)   
        num = num//10
    return sum
        
num = int(input())
res = num     
while(res != 1 and res != 4):    
    res = iHN(res)   
if(res == 1 or res==7):    
    print("True") 
else:    
    print("False") 