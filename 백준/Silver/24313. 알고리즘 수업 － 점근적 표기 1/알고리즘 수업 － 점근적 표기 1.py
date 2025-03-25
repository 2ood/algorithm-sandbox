import sys

f_a = list(map(int,sys.stdin.readline().strip().split()))
c = int(sys.stdin.readline().strip())
n_0 = int(sys.stdin.readline().strip())

f = f_a[0]*n_0+f_a[1]
f_1 =f_a[0]+f_a[1]
f_100 = f_a[0]*100+f_a[1]
cg = c*n_0

det = (f_a[0]-c)*n_0+f_a[1]
det100 = (f_a[0]-c)*100 +f_a[1]

if det <= 0 and det100<=0 :
    print(1)
else :
    print(0)