f = open("input", "r")
input = f.read()
print(input)
maxlLength = len(input)

i=3
while i < maxlLength:
    if len(set(input[i-3:i+1])) == 4:
        print(str(set(input[i-3:i+1])), input[i-3:i+1])
        break
    else:
        i += 1
print(i+1)