f = open("input", "r")
input = f.read()
my_list = input.splitlines()

isSchema = True
splitter = 4

cratesVertical = [0]

for i in range(0,9):
    cratesVertical.append([])

for line in my_list :
    if line == '':
        break
    else:
        cratesHorizontal = [line[i:i+splitter] for i in range(0, len(line), splitter)]
        column = 0
        for crate in cratesHorizontal:
            column += 1
            if '[' in crate:
                cratesVertical[column].insert(0,crate.strip("[] "))

isSchema = True
for line in my_list :
    if isSchema:
        if line == '':
            isSchema = False
    else:
        parameters = line.split()
        [quantity, pileFrom, pileTo] = [int(parameters[1]), int(parameters[3]), int(parameters[5])]

        print('========================================')
        print([quantity, pileFrom, pileTo])
        for i in range(0, quantity):
            cratesVertical[pileTo].append(cratesVertical[pileFrom][-1])
            cratesVertical[pileFrom].pop()
        for crates in cratesVertical:
            print(crates)

mdp = ''
for i in range(1, 10):
    mdp = mdp + str(cratesVertical[i][-1])
print(mdp)