#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Latihan 5: Generator PIN
#====================================================================================

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:",hasil)
        return
    
    for angka in ["0","1","2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)

'''
Penjelasan:
    Saat fungsi dijalankan. Base case akan mengecek parameter. Apabila tidak terpenuhi. Fungsi akan dilanjut dengan rekursi fungsi 
    dengan parameter hasil ditambahkan dengan elemen yang terdapat pada loop for. fungsi akan terus mengalami rekursi sampai base case terpenuhi dan seluruh
    elemen pada loop for berhasil memanggil rekursi fungsi
'''