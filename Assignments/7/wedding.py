import random  

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'elii', 'goli', 'mary', 'mina']


maried_boys = []
maried_girls = []
result = []
while len(girls) != 0:
    x = random.randint(0, len(boys) - 1)
    y = random.randint(0, len(girls) - 1)
    maried_boys.append(boys[x])
    maried_girls.append(girls[y])
    boys.remove(boys[x])
    girls.remove(girls[y])
for i in range(len(maried_girls)):
    result.append('(' + maried_boys[i] + ', ' + maried_girls[i] + ')')
print(result)