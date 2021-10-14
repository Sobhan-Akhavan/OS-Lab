import random
from random import randrange

i = 0
flag_exit = True
score = [0,0]
while i < 5:
    print("0. rock\n1. paper\n2. scissor")
    num = int(input("enter your choice: "))
    system_num = random.randrange(3)
    if num == 0 and system_num == 1:
        print("you-> rock")
        print("system-> paper")
        print("system win")
        score[1] += 1
    elif num == 1 and system_num == 2:
        print("you-> paper")
        print("system-> scissor")
        print("system win")
        score[1] += 1
    elif num == 2 and system_num == 0:
        print("you-> scissor")
        print("system-> rock")
        print("system win")
        score[1] += 1
    elif num == system_num:
        print("equal")
    else:
        if(system_num == 0):
            print("system-> rock")
        elif(system_num == 1):
            print("system-> paper")
        elif(system_num == 2):
            print("system-> scissor")
        print("you win")        
        score[0] += 1
    i += 1
if score[0] > score [1]:
    print("congratulations, you are winner")
else:
    print("keep trying, you will winner next time")


        

    