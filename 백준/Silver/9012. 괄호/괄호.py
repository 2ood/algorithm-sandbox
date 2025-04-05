import sys

iteration = int(sys.stdin.readline().strip())
 
for _ in range(iteration):
    stack = []
    test_str = sys.stdin.readline()
    flag = True

    for ch in test_str:
        if ch == '(':
            stack.append('(')
        if ch == ')':
            if stack:
                stack.pop()
            elif not stack:
                flag = False
                break
    if not stack and flag:
        print('YES')
    elif stack or not flag:
        print('NO')