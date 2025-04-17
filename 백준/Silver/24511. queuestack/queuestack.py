import sys
from collections import deque

n = int(sys.stdin.readline())
types = list(map(int, sys.stdin.readline().split()))
values = list(map(int, sys.stdin.readline().split()))

dq = deque()

for i in range(n):
    if types[i] == 0:
        dq.append(values[i])

m = int(sys.stdin.readline())
incoming = list(map(int, sys.stdin.readline().split()))

for num in incoming:
    dq.appendleft(num)
    print(dq.pop())
