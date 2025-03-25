import sys

grid = [ [0]*100 for i in range(100)]

paper_count = int(sys.stdin.readline().strip())

for k in range(paper_count) :
    i,j = list(map(int,sys.stdin.readline().strip().split()))
    for n in range(10):
        for m in range(10):
            grid[i+n][j+m] =1

count = 0

for n in range(100):
    for m in range(100) :
        count+=grid[n][m]

print(count)