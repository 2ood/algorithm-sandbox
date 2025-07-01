import sys
from collections import deque

#N,K = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
lines = []
counts = [0,0]

for i in range(N):
    lines.append(list(map(int,sys.stdin.readline().split())))

def color(lines,row_from,col_from,width,counts):
    universal_color = is_same_color(lines,row_from,col_from,width)
    if width==1 or universal_color>=0:
        counts[universal_color]+=1
        return counts
    
    else:
        new_width = width//2
        color(lines,row_from,col_from,new_width,counts)
        color(lines,row_from,col_from+new_width,new_width,counts)
        color(lines,row_from+new_width,col_from,new_width,counts)
        color(lines,row_from+new_width,col_from+new_width,new_width,counts)

        return counts
    
def is_same_color(lines,row_from,col_from,width):
    color_num = lines[row_from][col_from]

    for row in range(row_from,row_from+width):
        for col in range(col_from,col_from+width):
            if lines[row][col]!=color_num:
                return -1
            
    return color_num

counts = color(lines,0,0,N,counts)
print(str(counts[0]))
print(str(counts[1]))