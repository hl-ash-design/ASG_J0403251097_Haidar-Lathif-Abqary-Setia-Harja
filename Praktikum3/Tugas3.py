class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, data):
        self.head = None
        self.tail = None

    def insert_at_end(self, nodes):
        data = nodes.replace(" ", "").split(",")
        for item in data:
            new_node = Node(item)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
    
    def search_node(self, key):
        current = self.head
        found = False
        while current:
            if current.data == key:
                print(f"Elemen '{key}' ditemukan dalam Doubly Linked List.")
                found = True 
                return
            current = current.next
        if not found:
            print(f"Elemen '{key}' tidak ditemukan dalam Doubly Linked List.")

dll = DoublyLinkedList(None) #menyiapkan objek Doubly Linked List kosong
dll = DoublyLinkedList(None) #menyiapkan objek Doubly Linked List kosong
dll.insert_at_end(input("Masukkan elemen ke dalam Doubly Linked List: "))
dll.search_node(input("Masukkan elemen yang ingin dicari: "))