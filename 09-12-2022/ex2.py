def moveTail(xHead, yHead, xTail, yTail, travel = None):
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
    if travel is not None:
        if not (str(newXTail) + ',' + str(newYTail) in travel):
            travel.append(str(newXTail) + ',' + str(newYTail))
        return [newXTail, newYTail, travel]
    else:
        return [newXTail, newYTail]


####################################################
f = open("input", "r")
input = f.read()
my_list = input.splitlines()

coords = [[0,0] for i in range(10)]
travel = []
for i in range(len(coords)-1):
    moveTail(coords[i][0], coords[i][1], coords[i+1][0], coords[i+1][1], travel)

for line in my_list:
    command = line.split()
    direction = command[0]
    distance = int(command[1])
    for i in range(distance):
        match direction:
            case 'U':
                coords[0][1] -= 1
            case 'D':
                coords[0][1] += 1
            case 'L':
                coords[0][0] -= 1
            case 'R':
                coords[0][0] += 1
        for i in range(len(coords)-1):
            if (i == len(coords)-2):
                [coords[i+1][0], coords[i+1][1], travel] = moveTail(coords[i][0], coords[i][1], coords[i+1][0], coords[i+1][1], travel)
            else:
                [coords[i+1][0], coords[i+1][1]] = moveTail(coords[i][0], coords[i][1], coords[i+1][0], coords[i+1][1])
    # print(coords)

print(len(travel))
