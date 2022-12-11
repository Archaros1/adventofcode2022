f = open("input", "r")
input = f.read()
my_list = input.splitlines()

letterScores = {}
score = 0
for i in range(ord('a'), ord('z')+1):
    score += 1
    letterScores[chr(i)] = score
for i in range(ord('A'), ord('Z')+1):
    score += 1
    letterScores[chr(i)] = score

total = 0

group = []
lineNumber = 0
for line in my_list :
    group.append(line)
    if lineNumber == 2:

        letters = [*group[0]]
        for letter in letters :
            if letter in group[1] and letter in group[2] :
                total += letterScores[letter]
                break
        group = []
    lineNumber = (lineNumber + 1) % 3

print(total)