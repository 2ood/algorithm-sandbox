import sys
from collections import deque

# N = int(sys.stdin.readline())
# a,b = map(int,sys.stdin.readline().split())
# numbers = list(map(int,sys.stdin.readline().split()))

N:int = int(sys.stdin.readline())
target_1, target_2 = map(int,sys.stdin.readline().split())

E:int = int(sys.stdin.readline())

edges = [[] for _ in range(N+1)]

for i in range(E) :
    parent, child = map(int,sys.stdin.readline().split())
    edges[parent].append(child)

def get_parent(edges,person) :
    for i in range(len(edges)) :
        if person in edges[i] :
            return i
    
    return -1

queue = deque([(target_1,0)])
visited = [False for _ in range(N+1)]


def bfs(queue, visited, target, edges):
    if len(queue) ==0 :
        return -1
    
    next_person,his_chon = queue.popleft()

    if next_person == target :
        return his_chon
    
    if not visited[next_person]:
        visited[next_person] = True
        
        parent = get_parent(edges,next_person)
        if parent!=-1 : 
            if not visited[parent]:
                queue.append((parent,his_chon+1))
        
        children = edges[next_person]
        for i in range(len(children)):
            if not visited[children[i]]:
                queue.append((children[i],his_chon+1))
        
        return bfs(queue,visited,target_2,edges)
            
print(str(bfs(queue,visited,target_2,edges)))
