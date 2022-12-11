import json

def currentDir(arbo, currentDirPath):
    directory = arbo
    for step in currentDirPath:
        directory = directory['content'][step]
    return directory

def getTotalSize(arbo, maxSize = 0):
    total = 0
    if arbo['type'] == 'file':
        return 0
    if maxSize == 0 or arbo['size'] <= maxSize:
        total += arbo['size']
    for key in arbo['content']:
        total += getTotalSize(arbo['content'][key], maxSize)
    return total

##########################################################

f = open("input-test", "r")
input = f.read()
my_list = input.splitlines()
arbo = {
    'type': 'dir',
    'size': 0,
    'content': {},
}
currentDirPath = []

# créer l'arbo
for line in my_list :
    if line == '$ ls':
        continue
    if line == '$ cd /':
        currentDirPath = []
    else:
        if (line.startswith('$ cd')):
            dest = line.split(' ')[2]
            if (dest == '..'):
                currentDirPath.pop()
            else:
                currentDirPath.append(dest)
        else:
            if (line.startswith('dir')):
                currentDir(arbo, currentDirPath)['content'][line.split(' ')[1]] = {
                    'type': 'dir',
                    'size': 0,
                    'content': {},
                }
            else:
                currentDir(arbo, currentDirPath)['content'][line.split(' ')[1]] = {
                    'type': 'file',
                    'size': int(line.split(' ')[0]),
                }
                for i in range(0, len(currentDirPath)+1):
                    currentDir(arbo, currentDirPath[0:i])['size'] += int(line.split(' ')[0])
                    print(currentDirPath[0:i])

print(getTotalSize(arbo))
print(arbo['size'])
