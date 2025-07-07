import sys

# N = int(sys.stdin.readline())
# a,b = map(int,sys.stdin.readline().split())
# numbers = list(map(int,sys.stdin.readline().split()))

K,N = map(int,sys.stdin.readline().split())

lines = []
for i in range(K):
    lines.append(int(sys.stdin.readline()))

def number_of_lan_lines(lines:list[int], length:int) -> int:
    sum = 0
    for i in range(len(lines)):
        sum += lines[i]//length
    
    return sum




length_from = 1
length_to = max(lines)

current_max_length = 0

while length_from <= length_to:
    length_middle = (length_from+length_to)//2
    middle_number_of_lines = number_of_lan_lines(lines,length_middle)

    if  middle_number_of_lines < N:
        length_to = length_middle-1
    else :
        current_max_length = length_middle
        length_from = length_middle + 1


print(str(current_max_length))