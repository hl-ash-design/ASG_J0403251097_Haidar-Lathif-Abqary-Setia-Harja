#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Latihan 3: Mencari Nilai Maksimum
#====================================================================================

def cari_maks(data,index=0):

    #Base case
    if index==len(data)-1:
        return data[index]
    #recursive case
    maks_sisa = cari_maks(data, index +1)
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
    
angka = [3,7,2,9,5]
print("Nilai Maksimum:", cari_maks(angka))

'''
Penjelasan:
    Saat fungsi hitung dipanggil, base case akan mengecek parameter yang dimasukkan. Apabila kondisi base case tidak
    terpenuhi, fungsi akan lanjut ke kode print untuk menunjukkan langkah fungsi sebelum melakukan rekursi. Fungsi
    akan melakukan rekursi dengan parameter dikurangi 1. Rekursi fungsi berhenti saat kondisi base case terpenuhi.
    Rekursif diselesaikan dengan print 'selesai' dan fungsi akan kembali ke fungsi sebelumnya. Fungsi tersebut akan
    menyelesaikan kode dangan menjalankan print keluar sampai kembali ke fungsi awal. 
'''