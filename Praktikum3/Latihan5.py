class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, el):
        data = el.replace(" ", "").split(",") #mengubah input menjadi list
        for item in data:
            new_node = Node(item)
            if not self.head: # Jika linked list kosong
                self.head = new_node
                self.tail = new_node #mengarahkan tail ke node baru
            else:
                self.tail.next = new_node #menhubungkan tail ke node baru
                self.tail = new_node

    def display(self): #menampilkan data langkah maju
        current = self.head
        while current: #selama current tidak kosong
            print(current.data, end=" -> ") #menampilkan node saat ini
            current = current.next #pindah ke node barikutnya
        print("Null")
    
    def display_reverse(self): #menampilkan data langkah mundur
        def _display_reverse(node): #fungsi rekursif untuk menampilkan mundur
            if node is None: 
                return 
                return 
            _display_reverse(node.next) #memanggil funsi sendiri ke node berikutnya
            print(node.data, end=" -> ") #menampilkan data node apabila rekursi selesai dijalankan
        
        _display_reverse(self.head)# memulai rekursi dari head
        print("Null")#mengakhiri tampilan Linked List
    
    def display_both(self):
        print("Linked List sebelum dibalik:")
        self.display()
        print("Linked List setelah dibalik:")
        self.display_reverse()

sll = SingleLinkedList()
sll.insert_at_end(input("Masukkan elemen ke dalam Single Linked List: "))
sll.display_both()