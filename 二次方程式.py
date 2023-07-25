import math

print("ax^+bx+c=0")
a = int(input("実数a:"))
b = int(input("実数b:"))
c = int(input("実数c:"))

D = b**2 - 4*a*c

print(D)

if D < 0:
    print("虚数解です")
    


else :
    x_1 = ( -b + math.sqrt(b**2 - 4*a*c) )/ 2*a
    x_2 = ( -b - math.sqrt(b**2 - 4*a*c) )/ 2*a
 
    f =  isinstance( math.sqrt(D) , int )

    if f == True:
        print(x_1,x_2)

    if f == False:
        print( -b ,"+ √",(b**2 - 4*a*c) ,"/" , 2*a ,"," , -b,"- √",(b**2 - 4*a*c ), "/" , 2*a)



    e = int(input("途中式あり…0/なし…1:"))

    if e == 0:
        print("(",-b,"+ √",b**2,"-",4*a*c,")","/",2*a)
        print("(",-b,"- √",b**2,"-",4*a*c,")","/",2*a)