class listNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


# Implementation for Doubly Linked list 
class LinkedList:
    def __init__(self):
        # init the list with "dummy" head and tail nodes which makes
        # edge cases forinsert and remove easier
        self.head = listNode(-1)
        self.tail = listNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertEnd(self, val):
        newNode = listNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

    def insertFront(self, val):
        newNode = listNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next 

        self.head.next.prev = newNode
        self.head.next = newNode
    
    # Remove first node after dummy head
    def removeFront(self):
        self.head.next.next.prev  = self.head
        self.head.next = self.head.next.next

    def removeEnd(self):
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.prev.next = self.tail
    
    # traversal 
    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, "->")
            curr = curr.next
        print()