#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Contoh rekusif 2: Tracing Masuk/Keluar
#====================================================================================

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:",n)   #fase stacking
    hitung(n-1)         #pemanggilan rekursif
    print("keluar:",n)  #fase unwindling

hitung(3)

'''
Penjelasan:
    Saat fungsi hitung dipanggil, base case akan mengecek parameter yang dimasukkan. Apabila kondisi base case tidak
    terpenuhi, fungsi akan lanjut ke kode print untuk menunjukkan langkah fungsi sebelum melakukan rekursi. Fungsi
    akan melakukan rekursi dengan parameter dikurangi 1. Rekursi fungsi berhenti saat kondisi base case terpenuhi.
    Rekursif diselesaikan dengan print 'selesai' dan fungsi akan kembali ke fungsi sebelumnya. Fungsi tersebut akan
    menyelesaikan kode dangan menjalankan print keluar sampai kembali ke fungsi awal. 
'''