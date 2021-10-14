import random
from random import randrange

i = 0
flag_exit = True
score = [0,0,0]
players = ["user", "system 1", "system 2"]
while i < 5:
    print("0. front\n1. back")
    num = int(input("enter your choice: "))
    system_num = random.randrange(2)
    system_num2 = random.randrange(2)
    if num == 0 and (system_num == 1 and system_num2 == 1):
        print("you win")
        score[0] += 1
    elif num == 1 and (system_num == 0 and system_num2 == 0):
        print("you win")
        score[0] += 1
    elif system_num == 0 and (num == 1 and system_num2 == 1):
        print("system 1 win")
        score[1] += 1
    elif system_num == 1 and (num == 0 and system_num2 == 0):
        print("system 1 win")
        score[0] += 1
    elif system_num2 == 0 and (num == 1 and system_num == 1):
        print("system 2 win")
        score[2] += 1
    elif system_num2 == 1 and (num == 0 and system_num == 0):
        print("system 2 win")
        score[2] += 1    
    elif num == system_num == system_num2:
        print("equal")
    else:
        print("your choice is wrong.")
    i += 1

print("the winner is: ",players[score.index(max(score))])
        

    