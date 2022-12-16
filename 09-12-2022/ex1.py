def moveTail(xHead, yHead, xTail, yTail, travel):
    newXTail = xTail
    newYTail = yTail
    longueurX = xHead - xTail
    longueurY = yHead - yTail
    if not ((abs(longueurX) <= 1 and abs(longueurY) <= 1)):
        if (xHead - newXTail >= 1):
            newXTail += 1
        if (xHead - newXTail <= -1):
            newXTail -= 1
        if (yHead - newYTail >= 1):
            newYTail += 1
        if (yHead - newYTail <= -1):
            newYTail -= 1
    if not (str(newXTail) + ',' + str(newYTail) in travel):
        travel.append(str(newXTail) + ',' + str(newYTail))
    return [newXTail, newYTail, travel]


####################################################
f = open("input", "r")
input = f.read()
my_list = input.splitlines()

xHead = 0
yHead = 0
xTail = 0
yTail = 0
travel = []
moveTail(xHead, yHead, xTail, yTail, travel)

for line in my_list:
    command = line.split()
    direction = command[0]
    distance = int(command[1])
    for i in range(distance):
        match direction:
            case 'U':
                yHead -= 1
            case 'D':
                yHead += 1
            case 'L':
                xHead -= 1
            case 'R':
                xHead += 1
        [xTail, yTail, travel] = moveTail(xHead, yHead, xTail, yTail, travel)

print(len(travel))

# grid = []
# for i in range(6):
#     grid.append([i])
#     for j in range(6):
#         if (i == 0 and j == 0):
#             grid[i].append('s')
#             continue
#         if (str(j) + ',' + str(-i) in travel):
#             grid[i].append('#')
#         else:
#             grid[i].append('.')

# for lineG in reversed(grid):
#     print(lineG)