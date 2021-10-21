import math

number = input('Enter your number: ')
num = 0
for digit in number:
    num += math.pow(int(digit), int(len(number)))
if int(num) == int(number):
    print('Yes')
else:
    print('No')