<<<<<<< HEAD
'''
======================================================================
Praktikum 1: Konsep ADT dan data handling
Latihan dasar 1: Membaca seluruh isi file data
======================================================================
'''

#Membuka file semua
print("===Membuka file dalam satu string===")
with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    content=file.read()
print("=== Hasil read ===")
print(content)
print(f"tipe data: {type(content)}")

print()
#Membuka file per baris
print("===Membuka file per baris===")
Jumlah_baris = 0
with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    for baris in file:
        Jumlah_baris = Jumlah_baris+1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("baris ke-", Jumlah_baris)
        print("isinya:", baris)
print()

#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom-kolom data
print('===Membuka file ...===')
with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        NIM,nama,nilai = baris.split(",") #Memecah menjadi satuan dan manyimpannya dalam variabel
        print(f"NIM: {NIM} | Nama: {nama} | Nilai: {nilai}") #Menampilkan data dalam satu kolom


'''
=======================================================================
Praktikum 1: Konsep ADT dan data handling
Latihan dasar 2: Membaca data dan menyimpannya dalam struktur data list
=======================================================================
'''

data_list = [] #inisialisasi list untuk menampung data
with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        NIM,nama,nilai = baris.split(",") #Memecah menjadi satuan dan manyimpannya dalam variabel
        data_list.append([NIM,nama,int(nilai)])#Menyimpan data ke list
print("=== menampilkan list ===")
print(data_list)
print("contoh data pertama:", data_list[0])
print("contoh data ke-2:", data_list[1])
print("Jumlah Record pad list:", len(data_list))

#=======================================================================
#Praktikum 1: Konsep ADT dan data handling
#Latihan dasar 4: Membaca data dan menyimpannya ke struktur dictionary
#=======================================================================


data_dict = {} #inisialisasi dictionary

with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        NIM,nama,nilai = baris.split(",") #Memecah menjadi satuan dan manyimpannya dalam variabel
        data_dict[NIM] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print ("=== Menampilkan Data Dictionary ===")
print(data_dict)

#=======================================================================
#Praktikum 1: Konsep ADT dan data handling
#Latihan dasar 4: Membaca data dan menyimpannya ke struktur dictionary
#=======================================================================

=======
'''
======================================================================
Praktikum 1: Konsep ADT dan data handling
Latihan dasar 1: Membaca seluruh isi file data
======================================================================
'''

#Membuka file semua
print("===Membuka file dalam satu string===")
with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    content=file.read()
print("=== Hasil read ===")
print(content)
print(f"tipe data: {type(content)}")

print()
#Membuka file per baris
print("===Membuka file per baris===")
Jumlah_baris = 0
with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    for baris in file:
        Jumlah_baris = Jumlah_baris+1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("baris ke-", Jumlah_baris)
        print("isinya:", baris)
print()

#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom-kolom data
print('===Membuka file ...===')
with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        NIM,nama,nilai = baris.split(",") #Memecah menjadi satuan dan manyimpannya dalam variabel
        print(f"NIM: {NIM} | Nama: {nama} | Nilai: {nilai}") #Menampilkan data dalam satu kolom


'''
=======================================================================
Praktikum 1: Konsep ADT dan data handling
Latihan dasar 2: Membaca data dan menyimpannya dalam struktur data list
=======================================================================
'''

data_list = [] #inisialisasi list untuk menampung data
with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        NIM,nama,nilai = baris.split(",") #Memecah menjadi satuan dan manyimpannya dalam variabel
        data_list.append([NIM,nama,int(nilai)])#Menyimpan data ke list
print("=== menampilkan list ===")
print(data_list)
print("contoh data pertama:", data_list[0])
print("contoh data ke-2:", data_list[1])
print("Jumlah Record pad list:", len(data_list))

#=======================================================================
#Praktikum 1: Konsep ADT dan data handling
#Latihan dasar 4: Membaca data dan menyimpannya ke struktur dictionary
#=======================================================================


data_dict = {} #inisialisasi dictionary

with open("Data-Mahasiswa.txt",'r',encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        NIM,nama,nilai = baris.split(",") #Memecah menjadi satuan dan manyimpannya dalam variabel
        data_dict[NIM] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print ("=== Menampilkan Data Dictionary ===")
print(data_dict)

#=======================================================================
#Praktikum 1: Konsep ADT dan data handling
#Latihan dasar 4: Membaca data dan menyimpannya ke struktur dictionary
#=======================================================================

>>>>>>> e566c9d (Penambahan files)
