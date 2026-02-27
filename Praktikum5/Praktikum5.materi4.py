#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
#====================================================================================

def biner(n, hasil=""):
    #Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    #Choose + Explore: tambah '0'
    biner(n, hasil+"0")

    #Choose + Explore: tambah '1'
    biner(n, hasil+"1")

biner(3)

'''
Penjelasan:
    Saat fungsi dijalankan. Base case akan mengecek parameter. Apabila tidak terpenuhi. Fungsi akan dilanjut dengan rekursi dengan
    tambahan nilai '0'. rekursi akan berlangsung sampai base case terpenuhi. Kemudian fungsi akan terus kembali mengalami rekursi
    sampai semua rekursi memenuhi kondisi base case
'''