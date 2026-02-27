#====================================================================================
# Nama    : Haidar Lathif Abqary Setia Harja
# NIM     : J0403251097
# Kelas   : A2
#====================================================================================

#====================================================================================
# Latihan 1: Rekursif Pangkat
#====================================================================================

def pangkat(a,n):
    #Base case
    if n == 0:
        return 1
    
    #recursive case
    return a * pangkat(a,n-1)

print(pangkat(2,4)) #output: 16

'''
Penjelasan: 
    Saat fungsi dijalankan. Base case akan mengecek parameter. Apabila tidak terpenuhi. Fungsi akan dilanjut dengan rekursi dengan 
    parameter n dikurang satu. Rekursi fungsi berlanjut sampai parameter n memenuhi base case yang mengakibatkan operasi kembali ke
    fungsi sebelumnya. Nilai yang kembali dioperasikan oleh kode return fungsi sebelumnya sampai kembali ke fungsi awal. Hasil perkalian
    kemudian ditampilkan oleh kode print
'''