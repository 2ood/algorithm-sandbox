import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int,sys.stdin.readline().split()))
target = int(sys.stdin.readline().strip())

count = 0

for i in range(n) :
    if numbers[i] ==target :
        count+=1

print(count)  
