class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    

class MyLinkedList:
    def __init__(self):                  
        self.dummy_head = Node(0)
        self.dummy_tail = Node(0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
    

    def addAtHead(self, val):            
        new_node = Node(val)
        curr = self.dummy_head
         
        new_node.next, new_node.prev = curr.next, curr
        curr.next = new_node.next.prev = new_node
        pass
    

    def addAtTail(self,val):
        new_node = Node(val)
        curr = self.dummy_tail

        new_node.next, new_node.prev = curr, curr.prev
        curr.prev = new_node.prev.next = new_node
        pass


    def addAtIndex(self, idx, val):
        new_node = Node(val)
        curr = self.dummy_head.next

        while curr and idx:
            curr = curr.next
            idx -= 1
        
        if curr and not idx:
            new_node.next, new_node.prev = curr, curr.prev
            curr.prev = new_node.prev.next = new_node
    

    def deleteAtIndex(self, idx):
        curr = self.dummy_head.next
        
        while curr and idx:
            curr = curr.next
            idx -= 1
        
        if curr and not idx and curr is not self.dummy_tail:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

    
    def get(self, idx):
        curr = self.dummy_head.next

        while curr and idx:
            curr = curr.next
            idx -= 1
        if curr and not idx and curr is not self.dummy_tail:
            return curr.data
        return -1


            



