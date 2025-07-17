import sys
from collections import deque

# N = int(sys.stdin.readline())
# a,b = map(int,sys.stdin.readline().split())
# numbers = list(map(int,sys.stdin.readline().split()))

N:int = int(sys.stdin.readline())

store = [-1] * (N+1)

for num in range(1,N+1) :
    if num ==1 :
        store[num]=0
    elif num <=3 :
        store[num]=1
        continue
    
    min_dp = store[num-1]
    if num%2==0 :
        min_dp = min(min_dp,store[num//2])
    if num%3==0 :
        min_dp = min(min_dp,store[num//3])
    
    store[num]=min_dp+1

print(store[N])