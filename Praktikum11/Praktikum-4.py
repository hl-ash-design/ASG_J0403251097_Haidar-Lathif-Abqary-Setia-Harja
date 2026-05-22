#Nama : Haidar Lathif Abqary Setia Harja
#NIM : J0403251097
#Kelas : A2
def JalanKotaMatrix(kota, jalan): #membuat fungsi pembuatan matriks
    graph = [[0 for i in range(len(kota))] for j in range(len(kota))] #inisialisasi matriks
    for a, t in jalan: #mengisi matriks jika kota bersambung
        #mengkonversi nama kota menjadi index untuk mengisi matriks
        index_a = kota.index(a)
        index_t = kota.index(t)
        #mengisi matriks menggunakan index kota yang bersambung
        graph[index_a][index_t] = 1
        graph[index_t][index_a] = 1
    return graph

def JalanKotaList(kota, jalan): #membuat fungsi pembuatan list
    graph = {i: [] for i in kota} #inisialisasi list menggunakan dictionary
    for a, t in jalan: #mengisi list jika kota bersambung
        #mengisi list dengan nama kota yang bersambung
        graph[a].append(t)
        graph[t].append(a)
    return graph

if __name__ == "__main__":
    kota = ["Binjai", "Medan", "Tebing Tinggi", "Pematang Siantar", "Lima Puluh","Kisaran Timur","Balige"] #daftar kota
    jalan = [("Binjai","Medan"),("Binjai","Tebing Tinggi"),("Medan","Tebing Tinggi"),("Tebing Tinggi","Pematang Siantar"),("Tebing Tinggi","Lima Puluh"),("Lima Puluh","Kisaran Timur"),("Pematang Siantar","Balige")] #daftar jalan antar kota
    List_graph = JalanKotaList(kota, jalan) #memanggil fungsi pembuatan list
    Matrix_graph = JalanKotaMatrix(kota, jalan) #memanggil fungsi pembuatan matriks
    #menampilkan hasil
    print("Hubungan antar kota dalam bentuk matriks dan list adjacency:")
    print("\nMatriks Adjacency:")
    for row in range(len(kota)):
        for col in range(len(kota)):
            print(Matrix_graph[row][col], end=" ")
        print()

    print("\nList Adjacency:")
    for vertex in kota:
        print(f"{vertex}: {List_graph[vertex]}")

'''
Analisis singkat:
1. Jenis graph: Graph tidak berarah (undirected graph) karena hubungan antar kota bersifat dua arah.
2. Alasan memilih edge: merepresentasikan jalan asli antar kota yang ada di peta.
3. Representasi yang lebih cocok: List adjacency lebih cocok karena lebih efisien dalam menyimpan informasi dan hubungan antar kota cenderung linear (terhubung dalam satu jalan dua arah).
4. Kategori graph: Graph termasuk dalam kategori parse graph karena jumlah edge cenderung sedikit dibandingkan dengan jumlah vertex.  
'''