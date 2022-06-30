def compound_rate(PV, CRate, tp):  
    TotalAmount = PV * (pow ((1 + CRate / 100), tp))
    CInterest = TotalAmount - PV  
    print('%0.2f'%TotalAmount)
    
PV,CRate,tp =map(float,input().split())  
compound_rate(PV, CRate, tp) 