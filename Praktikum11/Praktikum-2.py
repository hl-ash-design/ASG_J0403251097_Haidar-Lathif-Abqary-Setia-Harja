#Nama : Haidar Lathif Abqary Setia Harja
#NIM : J0403251097
#Kelas : A2
def listGraph(v, edges): #membuat fungsi pembuatan list
    graph = {i: [] for i in v} #inisialisasi list menggunakan dictionary
    for u, v in edges: #mengisi list jika vertex bersambung
        #vertex bersambung saling mengisi list
        graph[u].append(v)
        graph[v].append(u)
    return graph

if __name__ == "__main__":
    V = ["A", "B", "C", "D"] #daftar vertex
    edges = [("A","B"),("A","C"),("B","D"),("C","D")] #daftar edge antar vertex
    graph = listGraph(V, edges) #memanggil fungsi
    for vertex in V: #menampilkan isi list untuk setiap vertex
        print(f"{vertex}: {graph[vertex]}")
