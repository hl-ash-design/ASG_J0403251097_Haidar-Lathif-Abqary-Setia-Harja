#=========================================================
# Pertemuan 3: Konsep linked list
# Latihan 1: Operasi Single Linked List
#=========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # tambahkan pointer tail
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

# Contoh penggunaan
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.display()  # Output: 3 -> 5 -> 13 -> 2 -> Null

#=========================================================
# Pertemuan 3: Konsep linked list
# Latihan 2: Operasi Double Linked List
#=========================================================

class DNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("Null")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("Null")

# Contoh penggunaan
dll = DoublyLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)
dll.display_forward()   # Output: 3 <-> 5 <-> 13 <-> 2 <-> Null
dll.display_backward()  # Output: 2 <-> 13 <-> 5 <-> 3 <-> Null

#=========================================================
# Pertemuan 3: Konsep linked list
# Latihan 3: Operasi Circular Linked List
#=========================================================

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Contoh penggunaan
cll = CircularLinkedList()
cll.insert_at_end(3)
cll.insert_at_end(5)
cll.insert_at_end(13)
cll.insert_at_end(2)
cll.display()  # Output: 3 -> 5 -> 13 -> 2 -> (head)

#=========================================================
# Pertemuan 3: Konsep linked list
# Latihan 4: Operasi Double Circular Linked List
#=========================================================

class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display_forward(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

    def display_backward(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head.prev
        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current == self.head.prev:
                break
        print("(head)")

# Contoh penggunaan
dcll = DoubleCircularLinkedList()
dcll.insert_at_end(3)
dcll.insert_at_end(5)
dcll.insert_at_end(13)
dcll.insert_at_end(2)
dcll.display_forward()   # Output: 3 <-> 5 <-> 13 <-> 2 <-> (head)
dcll.display_backward()  # Output: 2 <-> 13 <-> 5 <-> 3 <-> (head)