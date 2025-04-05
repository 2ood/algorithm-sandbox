import sys

n = int(sys.stdin.readline())

for _ in range(n):
    keylog = sys.stdin.readline().strip()
    left = []
    right = []
    for i in keylog:
        match i :
            case "<" :
                if left:
                    right.append(left.pop())
            case ">" :
                if right:
                    left.append(right.pop())
            case "-" :
                if left:
                    left.pop()
            case _ :
                left.append(i)
            
    left.extend(reversed(right))
    print(''.join(left))