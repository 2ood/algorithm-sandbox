num = int(input())

for i in range(num):
    stars =  ""
    for j in range(i+1):
        stars+="*"
    print(stars)