import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0] * N for _ in range(N)]

# 사과 설정
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

L = int(sys.stdin.readline())
curve = deque()
for _ in range(L):
    X, C = sys.stdin.readline().split()
    curve.append((int(X), C))


x = 0
y = 0
snake = deque([(0, 0)])
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
time = 1
d = 0
board[x][y] = -1 

while True:
    nx = x + direct[d][0]
    ny = y + direct[d][1]

    if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 1:
            x = nx
            y = ny
            board[nx][ny] = -1
            snake.append((nx, ny))
        
        elif board[nx][ny] == 0:
            x = nx
            y = ny
            board[nx][ny] = -1
            snake.append((nx, ny))
            
            tail = snake[0]
            board[tail[0]][tail[1]] = 0
            snake.popleft()

        
        elif board[nx][ny] == -1:
            print(time)
            break
    
    else:
        print(time)
        break

    if curve and time == curve[0][0]:
        if curve[0][1] == 'L':
            d = (d-1) % 4
        elif curve[0][1] == 'D':
            d = (d+1) % 4
        curve.popleft()

    time += 1