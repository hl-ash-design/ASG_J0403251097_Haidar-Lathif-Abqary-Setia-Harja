#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Contoh rekusif 3: Menjumlahkan Elemen List
#====================================================================================

def jumlah_list(data, index=0):
    #Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
    #Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1)

print(jumlah_list([2,4,6,8])) #output: 20

'''
Penjelasan:
    Saat fungsi dipanggil. Base case akan mengecek parameter. Apabila tidak terpenuhi, fungsi akan dilanjut dengan
    kode return yang akan memanggil rekursi fungsi. Apabila base case sudah terpenuhi, fungsi akan kembali ke kode return
    fungsi sebelumnya dan mengoperasikan return dengan value sesuai index pada fungsi tersebut sebelum kembali ke fungsi
    sebelumnya sampai ke fungsi awal. nilai yang dikembalikan akan ditampilkan di console menggunakan print.
'''