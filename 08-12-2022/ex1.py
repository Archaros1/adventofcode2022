def isVisible(forest, x, y):
    if (y==0 or y == len(forest[x])-1 or x==0 or x == len(forest)-1):
        return True
    visible = {
        'west': True,
        'east': True,
        'north': True,
        'south': True,
    }
    hauteurCurrent = forest[x][y]
    for i in range(0, y):
        if (forest[x][i] >= hauteurCurrent):
            visible['west'] = False
            break
    for i in range(y+1, len(forest[x])):
        if (forest[x][i] >= hauteurCurrent):
            visible['east'] = False
            break
    for i in range(0, x):
        if (forest[i][y] >= hauteurCurrent):
            visible['north'] = False
            break
    for i in range(x+1, len(forest)):
        if (forest[i][y] >= hauteurCurrent):
            visible['south'] = False
            break
    if (not visible['north'] and not visible['south'] and not visible['east'] and not visible['west']):
        return False
    else:
        return True


####################################################
f = open("input", "r")
input = f.read()
forest = input.splitlines()

count = 0
for i in range(0, len(forest)):
    for j in range(0, len(forest[i])):
        if (isVisible(forest, i, j)):
            count += 1

print(count)