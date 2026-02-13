class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # tambahkan pointer tail
    
    def insert_at_end(self, el):
        data = el.replace(" ", "").split(",") #mengubah input menjadi list
        for item in data:
            new_node = Node(item)
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

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
            if temp is None:
                return
            prev.next = temp.next
            temp = None

ll = LinkedList()
ll.insert_at_end(input("Masukkan elemen ke dalam Linked List: "))
ll.display()
ll.delete_node(input("Masukkan elemen yang ingin dihapus: "))
ll.display()