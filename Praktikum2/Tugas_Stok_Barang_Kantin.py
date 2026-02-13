data_stok = "Stok_barang.txt" #inisialisasi file txt dalam variabel data_stok
def tampil_barang():
    dict_barang = {} #inisialisasi dictionary kosong
    with open(data_stok,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #penghapusan karakter newline
            idx,barang,jumlah = baris.split(",")#memisahkan data berdasarkan koma
            dict_barang[idx] = {"barang": barang, "jumlah": jumlah} #memasukkan data ke dalam dictionary
    return dict_barang #mengembalikan dictionary berisi data barang

tampil_data = tampil_barang() #menyimpan data barang ke dalam variabel tampil_data

def tampil_data_barang(dict_barang):
    print("\n=== DATA STOK BARANG KANTIN ===") #menampilkan header tabel
    print(f"{'Kode Barang' : <12} | {'Nama Barang' : <20} | {'Jumlah' : >7}") #menampilkan judul kolom
    print("-"*40) #menampilkan garis batas
    for idx in sorted(dict_barang.keys()): #menampilkan data barang secara terurut
        barang = dict_barang[idx]['barang']
        jumlah = dict_barang[idx]['jumlah']
        print(f"{idx : <12} | {barang : <20} | {jumlah : >7}")

#tampil_data_barang(tampil_data) #uji coba fungsi tampil_data_barang

def cari_barang(dict_barang):
    nama = input("Masukkan nama barang yang dicari: ")#meminta input nama barang dari user
    for idx in dict_barang.keys(): #mencari barang dalam dictionary
        if nama.lower().replace(" ","") == dict_barang[idx]['barang'].lower().replace(" ",""):
            print("Barang ditemukan")
            print(f"Kode Barang: {idx} | Nama Barang: {dict_barang[idx]['barang']} | Jumlah: {dict_barang[idx]['jumlah']}") #menampilkan barang hasil pencarian
            break
    else:
        print("Barang tidak ditemukan") #menampilkan pesan jika barang tidak ditemukan

#cari_barang(tampil_data) #uji coba fungsi cari_barang

def update_stok(dict_barang):
    kode = input("Masukkan kode barang yang akan diupdate: ") #meminta input kode barang dari user
    if kode in dict_barang.keys(): #memeriksa apakah kode barang ada dalam dictionary
        print(f"Barang ditemukan: {dict_barang[kode]['barang']} | Stok: {dict_barang[kode]['jumlah']}")
        try: #antisipasi input tidak berupa angka
            Stok_baru = int(input("Masukkan jumlah stok baru: ")) #meminta input stok baru dari user
            dict_barang[kode]['jumlah'] = Stok_baru #memperbarui stok barang dalam dictionary
            print("Stok barang berhasil diperbarui")
        except ValueError:
            print("Input tidak valid. Stok harus berupa angka")
    else:
        print("kode barang tidak ditemukan")

#update_stok(tampil_data) #uji coba fungsi update_stok

def tambah_barang(dict_barang):
    barang_baru = input("Masukkan barang baru: ") #meminta input nama barang baru dari user
    for idx in dict_barang.keys(): #antisipasi keberadaan barang ganda dalam dictionary
        if barang_baru.lower().strip() == dict_barang[idx]['barang'].lower().strip():
            print("Barang sudah ada dalam stok")
            break
    else:
        try: #antisipasi input tidak berupa angka
            jumlah_baru = int(input("Masukkan jumlah stok barang baru: ")) #input stok barang baru
            kode_baru = "BRG" + str(int(max(dict_barang.keys())[3:]) + 1).zfill(3) #membuat kode barang baru
            dict_barang[kode_baru] = {"barang": barang_baru, "jumlah": jumlah_baru}
            print("Preview:") #penampilan preview barang baru
            print(f"Kode Barang: {kode_baru} | Nama Barang: {barang_baru} | Jumlah: {jumlah_baru}")
            print("Barang baru berhasil ditambahkan")
        except ValueError:
            print("Input tidak valid. Stok harus berupa angka")

#tambah_barang(tampil_data) #uji coba fungsi tambah_barang

def hapus_barang(dict_barang):
    kode_hapus = input("Masukkan kode barang yang akan dihapus: ")
    if kode_hapus in dict_barang.keys(): #memeriksa apakah kode barang ada dalam dictionary
        konfirmasi = input(f"Apakah anda yakin ingin menghapus barang {dict_barang[kode_hapus]['barang']}? (Y/N): ") #memeriksa apakah user yakin ingin menghapus barang
        if konfirmasi.lower().strip() == 'y': #antisipasi input tidak sesuai
            del dict_barang[kode_hapus]
            print("Barang berhasil dihapus")
        elif konfirmasi.lower().strip() == 'n':
            print("Penghapusan barang dibatalkan")
        else:
            print("Input tidak valid. Penghapusan barang dibatalkan")
    else:
        print("Kode barang tidak ditemukan")

#hapus_barang(tampil_data) #uji coba fungsi hapus_barang

def simpan_data(dict_barang):
    with open(data_stok,"w",encoding="utf-8") as file: #membuka file dalam mode tulis
        for idx in sorted(dict_barang.keys()): #mengiterasikan dan menyimpan data secara terurut
            barang = dict_barang[idx]['barang']
            jumlah = dict_barang[idx]['jumlah']
            file.write(f"{idx},{barang},{jumlah}\n") #menulis data barang ke dalam file sesuaii format
        print("Data stok barang berhasil disimpan ke dalam file") #konfirmasi penyimpanan data

#simpan_data(tampil_data) #uji coba fungsi simpan_data

def main(): #fungsi utama program
    while True: #memastikan program terus berjalan
        print("\n=== MENU STOK BARANG KANTIN ===") #menampilkan menu utama
        print("1. Tampilkan Data Stok Barang")
        print("2. Cari Barang")
        print("3. Update Stok Barang")
        print("4. Tambah Barang Baru")
        print("5. Hapus Barang")
        print("6. Simpan Data Stok Barang")
        print("7. Keluar")
        print("-"*30) #menggambar baris batasan menu dan input

        pilihan = int(input("Pilih menu (1-7): ")) #meminta input pilihan menu dari user
        try:
            if pilihan == 1:
                tampil_data_barang(tampil_data)
            elif pilihan == 2:
                cari_barang(tampil_data)
            elif pilihan == 3:
                update_stok(tampil_data)
            elif pilihan == 4:
                tambah_barang(tampil_data)
            elif pilihan == 5:
                hapus_barang(tampil_data)
            elif pilihan == 6:
                simpan_data(tampil_data)
            elif pilihan == 7:
                print("Terima kasih telah menggunakan program Stok Barang Kantin")
                break
            else:
                print("Pilihan di luar jangkauan menu. Silahkan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silahkan masukkan angka sesuai pilihan menu.")

if __name__ == "__main__":
    main() #menjalankan fungsi utama program