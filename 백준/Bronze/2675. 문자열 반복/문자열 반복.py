cases = int(input())
prints = []
for i in range(cases):
    output = ""
    repeat, char = input().split()
    for j in range(len(char)) :
        for k in range(int(repeat)) :
            output+=char[j]
    prints.append(output)

for i in range(len(prints)) :
    print(prints[i])