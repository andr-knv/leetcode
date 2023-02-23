class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummy_node = Node(0)
    

    def addAtHead(self, val):
        new_node = Node(val)
        curr = self.dummy_node
        new_node.next = curr.next
        curr.next = new_node
    

    def addAtTail(self, val):
        curr = self.dummy_node

        while curr.next:
            curr = curr.next
        
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
    

    def addAtIndex(self, idx, val):
        curr = self.dummy_node

        while curr.next and idx:
            curr = curr.next
            idx -= 1
        if curr and idx == 0:
            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node


    def deleteAtIndex(self, idx):
        curr = self.dummy_node

        while curr.next and idx:
            curr = curr.next
            idx -= 1
        
        if curr.next and idx == 0:
            curr.next = curr.next.next

    def get(self, idx):
        curr = self.dummy_node

        while curr.next and idx:
            curr = curr.next
            idx -= 1
        if curr.next and idx == 0:
            return curr.next.data
        return -1
        


