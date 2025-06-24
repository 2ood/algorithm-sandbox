import sys

numbers = map(int,sys.stdin.readline().split())
sum = 0

for n in numbers:
    sum+=n

print(str(sum))
