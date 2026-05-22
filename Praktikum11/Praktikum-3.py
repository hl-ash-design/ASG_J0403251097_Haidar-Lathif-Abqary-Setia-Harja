#Nama : Haidar Lathif Abqary Setia Harja
#NIM : J0403251097
#Kelas : A2
def matrixtolist(matrix): #membuat fungsi konversi
    graph = {} #inisialisasi list menggunakan dictionary
    for i in range(len(matrix)): #membaca setiap baris matriks
        graph[i] = [] #inisialisasi list untuk setiap vertex yang bersambung
        for j in range(len(matrix[i])): #membaca setiap kolom dalam baris matriks
            #mengubah isi matriks menjadi list jika vertex bersambung
            if matrix[i][j] == 1:
                graph[i].append(j)
    return graph

if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ] #isi matriks yang akan dikonversi
    graph = matrixtolist(matrix) #menkonversi matriks menjadi list
    for vertex in graph: #menampilkan isi list untuk setiap vertex
        print(f"{vertex}: {graph[vertex]}")