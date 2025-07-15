import sys
from collections import deque

# N = int(sys.stdin.readline())
# a,b = map(int,sys.stdin.readline().split())
# numbers = list(map(int,sys.stdin.readline().split()))

N:int = int(sys.stdin.readline())
E:int = int(sys.stdin.readline())

edges: list[tuple[int,int]] = []

for i in range(E) :
    node_1,node_2 = map(int,sys.stdin.readline().split())
    edges.append((node_1,node_2))

edges.sort(key=lambda x: x[0])

visited:list[bool] = [False for _ in range(N+1)]

def get_children(edges:list[tuple[int,int]], node:int) -> list[int]:
    result = []

    for i in range(len(edges)):
        if edges[i][0] == node:
            result.append(edges[i][1])
        if edges[i][1] == node:
            result.append(edges[i][0])

    return result    

## BFS
queue = deque([1])

while len(queue) >0 :
    next_node:int = queue.popleft()
    if not visited[next_node]: 
        visited[next_node] = True
        children:list[int] = get_children(edges, next_node)
        for i in range(len(children)):
            if not visited[children[i]]:
                queue.append(children[i])

infected_count = 0
for i in range(N+1) :
    if visited[i] :
        infected_count+=1

infected_count-=1

print(str(infected_count))