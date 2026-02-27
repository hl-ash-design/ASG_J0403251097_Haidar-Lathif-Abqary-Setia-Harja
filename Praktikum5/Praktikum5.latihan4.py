#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Latihan 4: Kombinasi Huruf
#====================================================================================

def kombinasi(n, hasil=""):

    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n,hasil+"A")
    kombinasi(n,hasil+"B")

kombinasi(2)

'''
Penjelasan:
    Saat fungsi dijalankan. Base case akan mengecek parameter. Apabila tidak terpenuhi. Fungsi akan dilanjut dengan rekursi fungsi 
    dengan parameter ditambah 'A'. fungsi akan terus mengalami rekursi sampai base case terpenuhi dan fungsi 
    terakhir memanggil rekursi akhir
'''