#Attempt to implement a linked list in python

#SINGLY LINKED LIST IMPLEMENTATION

#Create an empty node class. Everytime we create a new node, we will use this class.
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
#Create the linked list class. Everytime we create a new linked list, we will use this class. This class will have a variety of different functions. 

class linked_list:
    #Initialise the linked list and set the head
    def __init__(self):
        self.head = None

    #The append function allows you to add data onto an existing linked list
    def append(self, data):
        new_node = node(data)
        
        #Check if head is empty or not
        if self.head == None:
            self.head = new_node
            return
        
        #If there is a list, we can append the new node like so
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        
    #Display the data
    def display_data(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    #Prepend the data
    def prepend_data(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    
    #Insert data after a specific point
    def insert_after_node(self, prev_node, data):
        #Check if the previous node exists
        if not prev_node:
            print('Previous node is not in the list')
            return
        new_node = node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

#Testing area
the_linked_list = linked_list()

the_linked_list.append(13)
the_linked_list.append(17)
the_linked_list.prepend_data(24)
the_linked_list.insert_after_node(the_linked_list.head.next, 18)

the_linked_list.display_data()
