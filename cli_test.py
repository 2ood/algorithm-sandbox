import sys

class Node :
    def __init__(self, content=1):
        self.next = None
        self.content = content
    
    def __str__(self) :
        return 
    
class CircularLinkedList :
    def __init__(self):
        self.pointed = Node()
        self.pointed.next = self.pointed
        self.length = 1
        
    def append(self, node):
        node.next = self.pointed.next
        self.pointed.next = node
        self.length +=1
    
    def pop(self, k=1):
        if self.length <= 0 : # empty
            raise Exception("the list is empty")

        elif self.length ==1 :
            popped_node = self.pointed
            self.pointed = None
            self.length =0
            return popped_node
        
        else :
            for i in range(k//self.length-1) :
                self.pointed = self.pointed.next
            popped_node = self.pointed.next
            self.pointed.next = popped_node.next
            self.length-=1
            return popped_node
    
    def __str__(self) :
        result_string = "<"
        while self.length !=0 :
            result_string+=str(self.pop())
            if self.length > 0 :
                result_string+=", "
            else :
                retuls_string+=">"
        
        return result_string
        


[n,m] = list(map(int,sys.stdin.readline().split()))

c_list = CircularLinkedList()
for i in range(2,n) :
    c_list.append(Node(i))

print(c_list)
