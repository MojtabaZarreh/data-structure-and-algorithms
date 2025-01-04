class Node:
    def __init__(self, info) -> None:
        self.info = info
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def Insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else: 
            c_node = self.head
            while(c_node.next):
                c_node = c_node.next
            c_node.next = new_node
    
    def Delete(self, val):
        c_node = self.head 
        if val == c_node.info:
            self.head = c_node.next
            return
        else:
            while(c_node): 
                if c_node.info == val: 
                    break 
                prev_node = c_node
                c_node = c_node.next 
                
            prev_node.next = c_node.next
            c_node = None
        
    def Update(self,node, val): 
        c_node = self.head
        while(c_node):
            if c_node.info == node:
                c_node.info = val
                break
            c_node = c_node.next
                              
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.info)
            current_node = current_node.next
            
llist = LinkedList()
llist.Insert(8)
llist.Insert(3)
llist.Insert(4)
llist.Insert(2) 
llist.Insert(1)
llist.Insert(13)
llist.Insert(61)
llist.Insert(12)
llist.Insert(14)
llist.Delete(1)
llist.Update(12,156)
llist.Insert(77)
llist.printLL() 

    
