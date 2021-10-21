number = int(input("Enter Your number: "))
i = 1
fact = 1
while fact < number:
    i += 1
    fact *= i
if fact == number:
    print('Yes')
else:
    print('No')
