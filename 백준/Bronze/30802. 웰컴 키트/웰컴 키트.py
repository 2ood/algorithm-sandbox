import math

persons = int(input())
sizes = list(map(int,input().split()))
shirt_bulk, pen_bulk = map(int,input().split())

bundle = 0
for i in range(6):
    bundle += math.ceil(sizes[i]/shirt_bulk)

print(bundle)
print(str(persons//pen_bulk)+" "+str(persons%pen_bulk))
