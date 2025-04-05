import sys

n = int(sys.stdin.readline())
expression = sys.stdin.readline().strip()
number = list()
stack = list()

for i in range(n):
    number.append(int(sys.stdin.readline()))


for element in expression:
    if element.isalpha():
        stack.append(number[ord(element) - 65])
    else :
        match element :
            case "+" :
                temp = stack.pop()
                temp += stack.pop()
                stack.append(temp)
            case "-" :
                temp = stack.pop()
                temp = stack.pop() - temp
                stack.append(temp)
            case "*" :
                temp = stack.pop()
                temp *= stack.pop()
                stack.append(temp)
            case "/" :
                temp = stack.pop()
                temp = stack.pop() / temp
                stack.append(temp)
            case _ :
                raise Exception("Unknown operator")

print(f'{stack.pop():0.2f}')