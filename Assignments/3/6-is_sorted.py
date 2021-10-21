data = []
x = int(input('Enter number of your list: '))
i = 0
while i < x:
    y = int(input())
    data.append(y)
    i += 1
if sorted(data) == data:
    print(sorted(data))
    print('Yse')
else:
    print(sorted(data))
    print('No')