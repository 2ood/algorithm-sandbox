def solution(li, fr, temp, to, num) :
    # print("moving from"+str(fr)+" to "+str(to)+"with amount"+str(num))

    if(num<=1) :
        li.append(move(fr,to))
        return 1
    else :
        t1 = solution(li, fr, to, temp, num-1)
        li.append(move(fr,to))
        t2 = solution(li, temp,fr,to, num-1)
        return t1+1+t2


def move(fr, to) :
    return str(fr)+" "+str(to)

progress = list()
print(solution(progress, 1,2,3,int(input())))

for i in range(len(progress)): 
    print(progress[i])