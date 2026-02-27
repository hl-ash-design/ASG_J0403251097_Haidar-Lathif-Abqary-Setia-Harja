#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Contoh rekusif 1: Faktorial
#====================================================================================

def faktorial(n):
    # Base case: berhenti ketika n = 0
    if n == 0:
        return 1
    # Recursive case: masalah diperkecil menjadi faktorial(n - 1)
    return n * faktorial(n-1)

print(faktorial(5)) #output: 120

'''
Penjelasan:
    saat fungsi faktorial dijalankan, nilai '5' akan dimasukkan ke dalam parameter 'n'. 'n' kemudian diperiksa
    oleh base case untuk mengecek apakah nilai 'n' sudah sama dengan nol. Jika tidak memenuhi, fungsi akan
    berlanjut dan menjalani rekursi dengan parameter yang berkurang 1. Fungsi akan terus mengalami rekursi 
    sampai ketentuan base case terpenuhi. Saat base case terpenuhi, proses rekursi fungsi akan selesai dan hasil pengembalian
    nilai yang didapat akan kembali ke kode 'return' di rekursi fungsi sebelumnya sampai ke fungsi awal. output yang
    keluar berupa hasil perkalian dari semua operasi pada kode 'return'
'''