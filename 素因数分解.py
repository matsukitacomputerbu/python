#素因数分解

from calendar import c


a = int(input('正の整数a:'))

b = 1

while a > b:
 
 b += 1
 


 if a % b == 0 :
    
    print(b)
    
    a = a/b
    
    b = 1