import sys
from collections import deque

n = int(sys.stdin.readline())
types = list(map(int, sys.stdin.readline().split()))
values = list(map(int, sys.stdin.readline().split()))

stackqueue = deque()

for i in range(n):
    if types[i] == 0:
        stackqueue.appendleft(values[i])

m = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))

for num in inputs:
    stackqueue.appendleft(num)
    print(stackqueue.pop())
