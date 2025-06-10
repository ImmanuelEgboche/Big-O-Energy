"""You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
"""


## List + Pointer

"""
- Keep the list of urls (self.history)
- Keep pointer (self.curr) to the current page
- When you visit, truncate everythin after curr and add the new URL
"""

# Visual
"""
Start:     ["a.com"]   curr = 0
Visit b:   ["a.com", "b.com"]   curr = 1
Visit c:   ["a.com", "b.com", "c.com"]   curr = 2
Back(1):   curr = 1 → "b.com"
Forward(1): curr = 2 → "c.com"
"""

class BrowserHistoryListAndPointer:
    def __init__(self, hompage):
        self.history = [hompage]
        self.curr = 0
    
    def visit(self, url):
        self.history = self.history[:self.curr +1] # Truncate forward history
        self.history.append(url)
        self.cur += 1

    def back(self, steps):
        self.curr = (0, - self.cur - steps)
        return self.history[self.curr]

    def forward(self, steps):
        self.curr = min(len(self.history) -1, self.curr + steps)
        return self.history[self.curr] 
# All operations on average are O(1) bar visit whivh is amortised

## Two Stacks 

"""
- One stack for back pages

- One stack for forward pages

- Store the current page in separate variable

"""

# Visual 

"""
Current: "a.com"
Visit b: back = ["a.com"], current = "b.com", forward = []
Back: forward = ["b.com"], current = "a.com"
Forward: back = ["a.com"], current = "b.com"

"""


class BrowserHistoryTwoStacks:
    def __init__(self, hompage):
        self.back_stack = []
        self.forward_stack =[]
        self.current = hompage
    
    def visit(self,steps):
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps):
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -=1
        return self.current
    
# Vist function is O(1) the rest ate O(k) where k is the steps moved

## Doubly Linked list

"""
- Create a Node class with val prev next

- Maintain a pointer curr to the current node 

- On visit, drop the entire forward chain and link in new node
"""

"""
Current: "a.com"
Visit b: back = ["a.com"], current = "b.com", forward = []
Back: forward = ["b.com"], current = "a.com"
Forward: back = ["a.com"], current = "b.com"
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowerHistoryDoublyLinkedList:
    def __init__(self, homepage):
        self.curr = Node(homepage)
    
    def visit(self, url):
        newNode = Node(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode
        # Drop the forward history
        self.curr.next = None

    def back(self, steps):
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
    
    def forward(self, steps):
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

# visit is O(1) where as back and forward are O(k) where k is how far they need to go back or forward