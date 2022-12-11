def points(him, result):
    signPoints = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    signStrongTo = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    signWeakTo = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    match result:
        # LOSE
        case 'X':
            return 0 + signPoints[signWeakTo[him]]
        # DRAW 
        case 'Y':
            return 3 + signPoints[him]
        # WIN
        case 'Z':
            return 6 + signPoints[signStrongTo[him]]


    

f = open("input", "r")
input = f.read()
my_list = input.splitlines()

myPoints = 0

for line in my_list :

    himAndResult = line.split()
    myPoints += points(himAndResult[0], himAndResult[1])

print('Mes points : ' + str(myPoints))
