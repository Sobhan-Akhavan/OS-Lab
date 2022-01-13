def printKhayam(n:int):

    arr = [[0 for x in range(n)] 
              for y in range(n)] 

    for line in range (0, n):
        for i in range (0, line + 1):

            if(i == 0 or i == line):
                arr[line][i] = 1
                print(arr[line][i], end = " ") 

            else:
                arr[line][i] = (arr[line - 1][i - 1] + 
                                arr[line - 1][i])
                print(arr[line][i], end = " ")             
        print("\n", end = "")


n = int(input("Please enter size Khayam = " ))
printKhayam(n)
