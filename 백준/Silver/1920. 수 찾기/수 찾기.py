import sys

def binary_search(numberlist, target, start, end) :

    if(start >= end) :
        return 1 if numberlist[start] ==target else 0
    
    new_index = (start+end)//2
    if target == numberlist[new_index] :
        return 1
    elif target > numberlist[new_index] :
        return binary_search(numberlist, target, new_index+1,end)
    else :
        return binary_search(numberlist, target, start, new_index-1)

n = int(sys.stdin.readline())
numberlist = list(map(int,sys.stdin.readline().split()))
numberlist.sort()

m = int(sys.stdin.readline())
targets = list(map(int,sys.stdin.readline().split()))

for i in range(int(m)) :
    print(binary_search(numberlist,targets[i],0,len(numberlist)-1))
