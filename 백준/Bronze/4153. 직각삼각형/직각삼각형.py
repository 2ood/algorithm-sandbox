answers = []
ended = False

while ended == False :
    a, b, c = map(int,input().split())
    if a==0 and b==0 and c==0 :
        ended = True
        break
    else :
        sum_of_squares =a*a+b*b+c*c
        if sum_of_squares ==2*a*a or sum_of_squares ==2*b*b or sum_of_squares ==2*c*c :
            answers.append("right")
        else : 
            answers.append("wrong")    
    
for i in range(len(answers)) :
    print(answers[i])