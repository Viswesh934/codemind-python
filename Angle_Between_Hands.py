n=input()
h=n[0]+n[1]
m=n[3]+n[4]
h=int(h)
m=int(m)
if h==12:
    h=0
if m==60:
    m=0
hrangle=0.5*(h*60+m)
mnangle=6*m
angle=abs(hrangle-mnangle)
angle=min(360-angle,angle)
print(angle)