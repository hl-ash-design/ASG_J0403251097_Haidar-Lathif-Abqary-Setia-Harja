#======================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#======================================================================================

#======================================================================================
# Implenetasi dasar: Queue
#======================================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinitialisasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke node berikutnya (awal=None)

class Queue:
    #buat konstruktor buat inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None #node paling belakang
    
    def is_empty(self):
        return self.front is None

    #membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data):
        nodeBaru = Node(data)

        #jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #jika queue tidak kosong, maka letakkan data baru ke setelah rear dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear yang baru
    
    def dequeue(self):
        #menghapus data dari depan (front)
        data_terhapus = self.front.data #lihat data paling depan
        #geser front ke node berikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi None, maka queue kosong
        #rear juga harus jadi None
        if self.front is None:
            self.rear = None
        return data_terhapus
    
    def peek(self):
        #melihat data paling atas tanpa menghapus
        if self.is_empty():
            print("Queue kosong, tidak bisa peek")
            return None
        return self.front.data

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#instantiasi Queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()