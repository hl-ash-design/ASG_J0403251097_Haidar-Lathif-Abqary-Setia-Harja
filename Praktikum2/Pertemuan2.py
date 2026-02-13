<<<<<<< HEAD
# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# Latihan 1:
# ==================================================

# variabel menyimpan data file
nama_file = "Data-Mahasiswa.txt"

def buka_file(nama_file):
    data_dict = {} #inisialisai 
    with open(nama_file,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #Menghilangkan karakter baris baru
        nim,nama,nilai = baris.split(",") #Memecah menjadi satuan dan manyimpannya dalam variabel
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
    return data_dict

#buka_data = buka_file(nama_file)
# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 2: membuat fungsi menampilkan data
# ==================================================

def tampilkan_data(data_dict):
    #membuat header table
    print("\n=== DATA MAHASISWA ===")
    print(f"{'NIM' : <10} | {'nama' : <12} | {'nilai' : >5} ") # mengatur ukuran kolom
    '''
    Untuk tampiilan yang rapi, atur lebar kolom
    {NIM: <10}
    {nama: <15}
    {int(nilai): >5}
    '''
    print("-"*32) # membuat garis
    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {int(nilai) : >5}")

#tampilkan_data(buka_data) # memanggil fungsi untuk menampilkan data

# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 3: membuat fungsi mencari data
# ==================================================

# membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicar
    nim_cari = input("masukkan NIM mahasiswa yang akan dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("=== DATA MAHASISWA DITEMUKAN ===")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("Data tidak ditemukan, Pastikan NIM yang dimasukan benar")

# memanggil fungsi cari data
#cari_data(buka_data)

# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 4: membuat fungsi update data
# ==================================================

#membuat fungsi update data
def ubah_data(data_dict):
    #awali dulu dengan mencari nim / data mahasiswa yang ingin di updat
    nim = input("masukkan NIM mahasiswa yang ingin diubah datanya : ").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (1-100): ")).strip()
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi
#ubah_data(buka_data)

# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 5: membuat fungsi menyimpan data
# ==================================================

def simpan_data(data_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
         for nim in sorted(data_dict.keys()):
             nama = data_dict[nim]["nama"]
             nilai = data_dict[nim]["nilai"]
             file.write(f"{nim},{nama},{nilai}")

#memanggil fungsi simpan data
#simpan_data(nama_file,buka_data)
#print("Data Berhasil Disimpan")

# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 6: membuat fungsi menyimpan data
# ==================================================

def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)

    while true:
        print("===MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan data ke file")
        print("5. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihasn == "1":
            tampilkan_data(buka_data) #memamnggil fs 2 menampilkan data

        elif pilihan == "2":
            cari_data(buka_data) # memanggil fs 3 mencari data

        elif pilihan == "3":
            ubah_data(buka_data) # memanggil fs 4 mengubah data

        elif pilihan == "4":
            simpan_data(nama_file, buka_data) # memanggil fs 5 menyimpan data ke file
            print("Data berhasil disimpan")

        elif pilihan == "5":
            print("Program Selesai")
            break
        
        else:
            print("Pilihan tidak valid. Silahkan Coba Lagi")

#if __name__ == "__main__":
=======
# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# Latihan 1:
# ==================================================

# variabel menyimpan data file
nama_file = "Data-Mahasiswa.txt"

def buka_file(nama_file):
    data_dict = {} #inisialisai 
    with open(nama_file,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #Menghilangkan karakter baris baru
            nim, nama, nilai = baris.split(",") #Memecah menjadi satuan dan manyimpannya dalam variabel
            data_dict[nim] = {
                "nama" : nama,
                "nilai" : int(nilai)
                }
    return data_dict

buka_data = buka_file(nama_file)
# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 2: membuat fungsi menampilkan data
# ==================================================

def tampilkan_data(data_dict):
    #membuat header table
    print("\n=== DATA MAHASISWA ===")
    print(f"{'nim' : <10} | {'nama' : <12} | {'nilai' : >5} ") # mengatur ukuran kolom
    '''
    Untuk tampiilan yang rapi, atur lebar kolom
    {NIM: <10}
    {nama: <15}
    {int(nilai): >5}
    '''
    print("-"*32) # membuat garis
    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {int(nilai) : >5}")

#tampilkan_data(buka_data) # memanggil fungsi untuk menampilkan data

# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 3: membuat fungsi mencari data
# ==================================================

# membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicar
    nim_cari = input("masukkan NIM mahasiswa yang akan dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("=== DATA MAHASISWA DITEMUKAN ===")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("Data tidak ditemukan, Pastikan NIM yang dimasukan benar")

# memanggil fungsi cari data
#cari_data(buka_data)

# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 4: membuat fungsi update data
# ==================================================

#membuat fungsi update data
def ubah_data(data_dict):
    #awali dulu dengan mencari nim / data mahasiswa yang ingin di updat
    nim = input("masukkan NIM mahasiswa yang ingin diubah datanya : ").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (1-100): ")).strip()
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi
#ubah_data(buka_data)

# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 5: membuat fungsi menyimpan data
# ==================================================

def simpan_data(data_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
         for nim in sorted(data_dict.keys()):
             nama = data_dict[nim]["nama"]
             nilai = data_dict[nim]["nilai"]
             file.write(f"{nim},{nama},{nilai}")

#memanggil fungsi simpan data
#simpan_data(nama_file,buka_data)
#print("Data Berhasil Disimpan")

# ==================================================
# Pertemuan 2: konsep ADT dan data handling (skenario)
# latihan 6: membuat fungsi menyimpan data
# ==================================================

def main():
    #load data otomatis saat program dimulai
    buka_data = buka_file(nama_file)

    while True:
        print("===MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan data ke file")
        print("5. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #memamnggil fs 2 menampilkan data

        elif pilihan == "2":
            cari_data(buka_data) # memanggil fs 3 mencari data

        elif pilihan == "3":
            ubah_data(buka_data) # memanggil fs 4 mengubah data

        elif pilihan == "4":
            simpan_data(nama_file, buka_data) # memanggil fs 5 menyimpan data ke file
            print("Data berhasil disimpan")

        elif pilihan == "5":
            print("Program Selesai")
            break
        
        else:
            print("Pilihan tidak valid. Silahkan Coba Lagi")

if __name__ == "__main__":
    main()
>>>>>>> e566c9d (Penambahan files)
