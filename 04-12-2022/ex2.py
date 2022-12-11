f = open("input", "r")
input = f.read()
my_list = input.splitlines()

count = 0

for line in my_list :
    [a1, a2] = line.split(',')
    [a1Bot, a1Top] = a1.split('-')
    [a2Bot, a2Top] = a2.split('-')
    overlap1 = False
    overlap2 = False
    for i in range(int(a1Bot), int(a1Top)+1):
        if i in range(int(a2Bot), int(a2Top)+1):
            print(i, a2)
            overlap1 = True
            break
    for i in range(int(a2Bot), int(a2Top)+1):
        if i in range(int(a1Bot), int(a1Top)+1):
            print(i, a1)
            overlap2 = True
            break
    
    if overlap1 or overlap2:
        count += 1

print(count)
