import math
r=int(input("enter the radius"))
area=3.142*r*r
print(area)
S1=int(input("enter the side1="))
S2=int(input("enter the side2="))
S3=int(input("enter the side3="))
S=(S1+S2+S3)/2.0
areaT=math.sqrt(S*(S-S1)*(S-S2)*(S-S3))
print(areaT)


    

