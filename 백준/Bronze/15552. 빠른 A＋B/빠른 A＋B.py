import sys

test_count = int(sys.stdin.readline().rstrip())

data = [sys.stdin.readline().rstrip().strip() for i in range(test_count)]

for i in range(len(data)) :
    ints = list(map(int,data[i].split()))
    print(ints[0]+ints[1])