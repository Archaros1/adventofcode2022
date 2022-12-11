def whoWin(him, me):
    signPoints = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    signWeakTo = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    if him == me:
        return 3 + signPoints[me]
    elif signWeakTo[him] == me:
        return 6 + signPoints[me]
    else:
        return signPoints[me]

f = open("input", "r")
input = f.read()
my_list = input.splitlines()

# Rock      : A X 1
# Paper     : B Y 2
# Scissors  : C Z 3

myPoints = 0
hisPoints = 0

for line in my_list :
    line = line.replace('X', 'A')
    line = line.replace('Y', 'B')
    line = line.replace('Z', 'C')

    himAndMe = line.split()
    myPoints += whoWin(himAndMe[0], himAndMe[1])
    hisPoints += whoWin(himAndMe[1], himAndMe[0])

print('Mes points : ' + str(myPoints))
print('Ses points : ' + str(hisPoints))

if myPoints > hisPoints:
    print("J'ai gagné !")
else:
    print("J'ai perdu !")
