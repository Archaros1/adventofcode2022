f = open("input", "r")
input = f.read()
my_list = input.splitlines()

count = 0

for line in my_list :
    [a1, a2] = line.split(',')
    [a1Bot, a1Top] = a1.split('-')
    [a2Bot, a2Top] = a2.split('-')
    fullyContain1 = True
    fullyContain2 = True
    for i in range(int(a1Bot), int(a1Top)+1):
        if i not in range(int(a2Bot), int(a2Top)+1):
            print(i, a2)
            fullyContain1 = False
            break
    for i in range(int(a2Bot), int(a2Top)+1):
        if i not in range(int(a1Bot), int(a1Top)+1):
            print(i, a1)
            fullyContain2 = False
            break
    
    if fullyContain1 or fullyContain2:
        count += 1

print(count)
