# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the front
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Print all nodes
    def print_all(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Create a linked list
ll = LinkedList()

# Add nodes
ll.push_front("Hana")
ll.push_front("Abel")
ll.push_front("Sara")
ll.push_front("Dawit")
ll.push_front("Almaz")

# Print the list
ll.print_all()