count = int(input())
numbers = list(map(int,input().split()))
min = numbers[0]
max = numbers[0]
for i in range(count) :
    if min > numbers[i] :
        min = numbers[i]
    if max < numbers[i]:
        max = numbers[i]

print(str(min)+" "+str(max))