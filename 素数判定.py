#素数判定

a = int (input ('正の数a:'))
b = 2

while a > b:
 
 b += 1
 
 if a % (b-1) == 0 :
    
    print('これは素数ではありません')
    break 

 if  a % b != 0: 
      continue
      
if a == 1:      
    print ('これは素数ではありません')

if a == b :
    print('これは素数である')