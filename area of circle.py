# import math
# r=int(input("enter the radius"))
# area=3.142*r*r
# print(area)
# S1=int(input("enter the side1="))
# S2=int(input("enter the side2="))
# S3=int(input("enter the side3="))
# S=(S1+S2+S3)/2.0
# areaT=math.sqrt(S*(S-S1)*(S-S2)*(S-S3))
# print(areaT)
# a=["ys",44,True,False]
# a1="sgajjjl"
# print(a[1:4])
# print(len.a1)
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    
    # Traverse the binary string from right to left
    for bit in reversed(binary):
        if bit == '1':
            decimal += 2 ** power
        power += 1
        
    return decimal

# Example usage
binary_number = int(input(enter the binry value))
if binary_number==1:
     
    elif binary_number==0:
    decimal_number = binary_to_decimal(binary_number)
    print(f"The decimal equivalent of binary {binary_number} is {decimal_number}")
    else print("vhdi")
    

