class Node :
    def __init__(self, content=1):
        self.next = None
        self.prev = None
        self.content = content
    
    def __str__(self) :
        return str(self.content)