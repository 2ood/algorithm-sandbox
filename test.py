test = [
    (["5 21"],"26"),
    (["10 500"],"510")
]

def max_sum(candidates, currently, target, cards) :
    if len(candidates) == 0 :
        return currently
    elif currently == target :
        return currently
    elif cards == 0 :
        return currently
    else :
        number = candidates.pop(0)
        without_this = max_sum(candidates,currently,target,cards)
        if currently+number > target :
            return without_this
        else :
            with_this = max_sum(candidates,currently+number,target,cards-1)
            return max(with_this, without_this)

def solve(input) :
    size, maximum = map(int,input[0].split())
    candidates = list(map(int,input[1].split()))
    
    return str(max_sum(candidates,0, maximum,3))
             
            
            
            



for i in range(len(test)) :
    solv = solve(test[i][0])
    print("input : "+str(test[i][0]))
    print("Expected : "+str(test[i][1]))
    print("Output : "+str(solv))
    
    try : 
        assert solv == test[i][1]
        print("test case "+str(i)+" passed")
    except :
        print("Error in test case "+str(i))
