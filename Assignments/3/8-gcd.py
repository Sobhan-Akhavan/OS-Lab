def computeGCD(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd
  
a = int(input('a = '))
b = int(input('b = '))
  
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60,48))