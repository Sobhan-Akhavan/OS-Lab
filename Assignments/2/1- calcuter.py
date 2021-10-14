import math


flag_exit = True
while flag_exit:
    number = float(input("enter your number: "))
    print("1. sinus \n2. cosinus \n3. tan \n4. cot \n5. log \n6. exit")
    case = int(input("enter your choice: " ))
    while True:
        if case == 1:
            print(math.sin(math.radians(number)))
            break
        elif case == 2:
            print(math.cos(math.radians(number)))
            break
        elif case == 3:
            print(math.tan(math.radians(number)))
            break
        elif case == 4:
            print(math.cot(math.radians(number)))
            break
        elif case == 5:
            print(math.log(number))
            break
        elif case == 6:
            flag_exit = False
            break
print("see you next time :)")
    
        
