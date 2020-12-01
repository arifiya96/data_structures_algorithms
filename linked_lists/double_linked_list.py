#Implementation of double linked list

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head == None:
            new_node = node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = node(data)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None
                         
    def prepend(self, data):
        new_node = node(data)
        if self.head == None:
            new_node.prev = None
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
    
    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

#Testing area

dbll = linked_list()
dbll.append(1)
dbll.append(2)
dbll.append(3)
dbll.append(4)
dbll.prepend(0)

dbll.print_list()

