class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5

    def __init__(self, value):
        """Initialize the stack with an empty state."""
        new_node = Node(value)
        self.rear = new_node
        self.top = new_node
        self.top.next = self.rear
        self.size = 1

    def push(self, value):
        """Add a new Temperature object to the stack, replacing the oldest entry if full."""
        new_node = Node(value)
        if self.size == 0:
            self.rear = new_node
            self.top = new_node
            self.top.next = self.rear
            self.size = 1
        elif self.size == self.MAX_SIZE:
            new_node.next = self.rear.next
            self.rear = new_node.next
            self.top.next = new_node
            self.top = new_node
        else:
            new_node.next = self.rear
            self.top.next = new_node
            self.top = new_node
            self.size += 1

    def pop(self):
        """Remove the oldest entry from the stack."""
        if self.size == 0:
            return None
        else:
            temp = self.rear
            if self.size == 1:
                self.rear = None
                self.top = None
                self.size = 0
                return temp
            self.top.next = self.rear.next
            self.rear = self.top.next
            self.size -= 1
            return temp

    def peek(self):
        """Return the most recent temperature entry without removing it."""
        return self.top

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        print()
        temp = self.rear
        for i in range(self.size):
            print(temp.data)
            temp = temp.next

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.size == 0
