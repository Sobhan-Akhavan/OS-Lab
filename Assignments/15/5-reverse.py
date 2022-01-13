array = list(map(int, input("input Array = ").split()))
isReverse = True 
for i in range(len(array)):
    if array[i] != array[-i-1]:
        isReverse = False

if isReverse :
    print("TRUE")
else:
    print("FALSE")
