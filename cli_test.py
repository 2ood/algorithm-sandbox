import sys

class Node :
    def __init__(self,content=None) :
        self.next = None
        self.prev = None
        self.content = content
    
    def __str__(self):
        return str(self.content)


class LinkedList :
    def __init__(self):
        self.head = Node()
        self.pointed = self.head

    def append(self,node):
        if self.head.content == None : #empty
            node.prev = self.head
            self.head = node
            self.pointed = node
            
        else :
            node.next = self.pointed.next
            self.pointed.next = node
            node.prev = self.pointed
            self.pointed = node


    def pop(self):
        popped_node = None
        if self.pointed.next == None:
            popped_node = self.pointed
            next_pointed = self.pointed.prev
            self.pointed.prev.next = None
            self.pointed = next_pointed

        elif self.pointed == self.head:
            popped_node = self.pointed
            next_pointed = self.pointed.next
            self.pointed.next.prev = self.head.prev
            self.pointed = next_pointed

        else : 
            popped_node = self.pointed
            self.pointed.next.prev = self.pointed.prev
            self.pointed.prev.next = self.pointed.next
            self.pointed = popped_node.prev
            
        return popped_node    

    def pointNext(self) :
        if self.pointed.next == None :
            return

        self.pointed = self.pointed.next 


    def pointPrev(self) :
        if self.pointed == self.head :
            return
        
        self.pointed = self.pointed.prev

    def deletePointed(self) :
        return self.pop()


    def __str__(self):
        return_list = []
        self.pointed = self.head
        while self.pointed.next != None:
            return_list.append(str(self.pointed))
            self.pointed = self.pointed.next
        
        return "".join(return_list)

n = int(sys.stdin.readline().strip())
result = []

for i in range(n) :
    keydown_string = list(sys.stdin.readline())
    key = LinkedList()

    for char in keydown_string :
        match char:
            case "<":
                key.pointPrev()
            case ">":
                key.pointNext()
            case "-":
                key.deletePointed()
            case _ :
                key.append(Node(char))

    result.append(key)

for j in range(len(result)) :
    print(str(result[j]))