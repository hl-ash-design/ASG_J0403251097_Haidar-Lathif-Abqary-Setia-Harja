#Nama : Haidar Lathif Abqary Setia Harja
#NIM : J0403251097
#Kelas : A2
def matrixGraph(v, edges): #membuat fungsi pembuatan matrikz
    graph = [[0 for i in range(v)] for j in range(v)] #inisialisasi matriks

    for u, v in edges: #mengisi matriks jika vertex bersambung
        #vertex bersambung saling mengisi baris dan kolom dalam matriks
        graph[u][v] = 1 
        graph[v][u] = 1
    return graph

if __name__ == "__main__":
    V = 4 #jumlah vertex
    edges = [(1,2),(0,1),(0,2),(2,3)] #daftar edge antar vertex
    graph = matrixGraph(V, edges) #memanggil fungsi
    for row in range(V):#menampilkan isi baris matriks
        for col in range(V): #menampilkan isi kolom per baris
            print(graph[row][col], end=" ") 
        print()