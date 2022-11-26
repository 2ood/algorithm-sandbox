import sys

sys.setrecursionlimit(10000)

def will_sk_win(num) :
    if(num>3):
        return not(lookup(num-2) and lookup(num-4))
    
    elif(num==1 or num==3) :
        return True

    else :
        return False

v = int(input())
cache = [-1]*v        

def lookup(index) :
    if(cache[index]!=-1) :
        return cache[index]
    else :
        cache[index] =will_sk_win(index+1)
        return cache[index]



print("SK" if will_sk_win(v) else "CY")