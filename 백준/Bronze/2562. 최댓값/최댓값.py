index = 1
max = -1
for i in range(9) :
    num = int(input())
    if max < num :
        max = num
        index = i+1

print(str(max))
print(str(index))