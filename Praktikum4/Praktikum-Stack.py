#======================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#======================================================================================

#====================================================================================
# Implenetasi dasar: Stack
#====================================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinitialisasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke node berikutnya (awal=None)

#stack ada operasi push(memasukkan head baru) dan pop(menghapus head)

class Stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
    
    def push(self, data):
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi / memanggil constructor pada class Node

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top ke node baru (head baru)
        self.top = nodeBaru

    def is_empty(self):
        return self.top is None #stack kosong jika top = None
    
    def pop(self): #mengambil / menghapus data paling atas (top/head)
        
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #simpan data yang akan dihapus (top saat ini)
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #melihat data paling atas tanpa menghapus
        if self.is_empty():
            print("Stack kosong, tidak bisa peek")
            return None
        return self.top.data

    def tampilkan(self):
        # Top -> A -> B
        current = self.top
        print(" Top ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

   





#instantiasi class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan() # Top -> C -> B -> A -> None
print("Peek:", s.peek()) # Peek: C
s.pop() # menghapus C
s.tampilkan() # Top -> B -> A -> None
print("Peek:", s.peek()) # Peek: B