class Stack:
  def __init__(self):
    self.items = []

  def push(self, val):
    self.items.append(val)

  def pop(self):
    try:                      # pop할 아이템이 없으면
      return self.items.pop()
    except IndexError:        # indexError 발생
      print("Stack is empty")

  def top(self):
    try:
      return self.items[-1]
    except IndexError:
      print("Stack is empty")

  def len_stack(self): # len() 호출하면 stack의 item 수 반환
    return len(self.items)

def get_token_list(expr):
  temp = []
  result = []
  num = str()
  num_temp = 0

  for idx,i in enumerate(expr):
    if i == '(' or i == ')' or i == '+' or i == '-' or i == '*' or i == '/':
      result.append(i)
    elif i == ' ':
      continue
    else:
      num_temp += int(i)
      if expr[idx+1].isdigit():
        num_temp *= 10
      else:
        result.append(float(num_temp))
        num_temp = 0
  return result

def infix_to_postfix(prob,opStack,outStack) :
    for i in prob:
        if i=="*" or i=="/" or i =="(":
            opStack.push(i)
        elif i=="+" or i=="-":
            if opStack.len_stack() == 0:
                opStack.push(i)
            else :
                for j in range(opStack.len_stack()):
                    if opStack.top() == "*" or opStack.top() == "/":
                        outStack.push(opStack.top())
                        opStack.pop()
                    opStack.push(i)
        
        elif i==")":
            while(opStack.top()!="(") :
                outStack.push(opStack.top())
                opStack.pop()
            opStack.pop()
        else :
            outStack.push(i)
    while(opStack.len_stack()!=0) :
        outStack.push(opStack.top())
        opStack.pop()
    
    return outStack.items


opStack = Stack()
outStack = Stack()

print(infix_to_postfix(get_token_list("(1+2*(3-4/5+6)-(7+8))"),opStack,outStack))