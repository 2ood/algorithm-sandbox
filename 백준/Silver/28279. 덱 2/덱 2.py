import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deck = deque()

for _ in range(n):
    command = input().strip().split()
    cmd = int(command[0])

    if cmd == 1:
        deck.appendleft(int(command[1]))
    elif cmd == 2:
        deck.append(int(command[1]))
    elif cmd == 3:
        print(deck.popleft() if deck else -1)
    elif cmd == 4:
        print(deck.pop() if deck else -1)
    elif cmd == 5:
        print(len(deck))
    elif cmd == 6:
        print(0 if deck else 1)
    elif cmd == 7:
        print(deck[0] if deck else -1)
    elif cmd == 8:
        print(deck[-1] if deck else -1)
