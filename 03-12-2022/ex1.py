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

for line in my_list :
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    firstpartLetters = [*firstpart]
    for letter in firstpartLetters :
        if letter in secondpart :
            total += letterScores[letter]
            break

print(total)