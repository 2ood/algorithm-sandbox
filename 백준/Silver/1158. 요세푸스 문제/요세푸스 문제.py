import sys

class Node :
    def __init__(self, content=1):
        self.next = None
        self.content = content
    
    def __str__(self) :
        return str(self.content)
    
class CircularLinkedList :
    def __init__(self):
        self.head = Node(1)
        self.pointed = self.head
        self.pointed.next = self.pointed
        self.length = 1
        
    def append(self, node):
        node.next = self.pointed.next
        self.pointed.next = node
        self.pointed = self.pointed.next
        self.length +=1
    
    def pop(self, k=1):
             
        if self.length <= 0 : # empty
            raise Exception("the list is empty")

        elif self.length == 1 :
            popped_node = self.head
            self.head = None
            self.pointed = None
            self.length = 0
            return popped_node
        
        else :
            iteration = k%self.length -2
            if iteration <0 :
                iteration+=self.length

            for _ in range(iteration) :
                self.pointed = self.pointed.next
                
            popped_node = self.pointed.next
            self.pointed.next = popped_node.next
            if popped_node == self.head :
                self.head = self.head.next
            self.length-=1
            self.pointed = self.pointed.next
            
            return popped_node
    
    def peek(self):
        return self.pointed
    
    def __iter__(self):
        return self.pointed
    
    def __next__(self) :
        return self.pointed.next
    
    def __str__(self) :
        result_string = "<"
        self.pointed = self.head
        
        for i in range(self.length) :
            result_string+=str(self.peek())
            self.pointed = self.pointed.next

            if i < self.length-1 :
                result_string+=", "
            else :
                result_string+=">"
        
        return result_string
        


[n,m] = list(map(int,sys.stdin.readline().split()))

c_list = CircularLinkedList()
for i in range(2,n+1) :
    c_list.append(Node(i))

josephus = []
c_list.pointed = c_list.head

for j in range(n):
    josephus.append(str(c_list.pop(m)))

print("<",", ".join(josephus),">",sep="")
