#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Implenetasi dasar: Node pada Linked List
#====================================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinitialisasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke node berikutnya (awal=None)

#1) membuat node dengan instantiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) mendefinisikan head dan menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Transversal : menelusuri Node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya


