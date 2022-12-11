f = open("input2", "r")
input = f.read()
my_list = input.splitlines()

groupedList = [0]

for line in my_list :
    if line == '' :
        groupedList.append(0)
    else :
        groupedList[len(groupedList)-1] += int(line)

top3 = sorted(groupedList)[len(groupedList)-3:]

print(groupedList)
print(sorted(groupedList))
print(top3)
print(sum(top3))