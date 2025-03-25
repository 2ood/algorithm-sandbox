import sys

size,iteration = list(map(int,sys.stdin.readline().strip().split()))

baskets = []

for k in range(size) :
    baskets.append(k+1)

for k in range(iteration) :
    i, j = list(map(int,sys.stdin.readline().strip().split()))
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

res = ""

for k in range(size) :
    res+=str(baskets[k])
    if k < size-1 : 
        res+=" "

print(res)