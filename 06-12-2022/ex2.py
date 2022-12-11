f = open("input", "r")
input = f.read()
print(input)
maxlLength = len(input)

beginning=14

for i in range(beginning-1, maxlLength+1):
    if len(set(input[i-13:i+1])) == 14:
        print(str(set(input[i-13:i+1])), input[i-13:i+1])
        break

print(i+1)