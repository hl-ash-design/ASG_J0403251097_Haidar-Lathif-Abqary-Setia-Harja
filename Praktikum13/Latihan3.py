# Nama  : Haidar Lathif Abqary Setia Harja
# NIM   : J0403250197
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree
# ===============================================================
# Implementaasi Sederhana Algoritma Prim
# ===============================================================

import heapq

# Daftar edge tiap verteks
graph = {
    'A': [('B', 4), ('C', 2), ('D', 5)],
    'B': [('A', 4), ('D', 3)],
    'C': [('A', 2), ('D', 1)],
    'D': [('A', 5), ('B', 3), ('C', 1)]
}

# membuat fungsi prim
def prim(graph, start):

    # memasukkan vertex pertama
    visited = set([start])

    edges = []

    # Memasukkan semua Vertex yang berhubungan dengan vertex awal
    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Mengeksekusi setiap edges pada graph
    while edges:
        
        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight
            # mengulangi prosedur pada setiap vertex yang berhubungan dengan vertex awal
            for neighbor, w in graph[v]:

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")

print(f"Total bobot: {total}")

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
# Node A

# 2. Edge mana yang dipilih pertama kali?
# Edge A-B

# 3. Bagaimana Prim menentukan edge berikutnya?
# Dengan menentukan edge yang terhubung dengan edge sebelumnya dengan nilai terkecil

# 4. Berapa total bobot MST yang dihasilkan?
# Total bobot tree adalah 6

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# Krustal membuat MST dengan menyortir dan menghubungkan edge dengan bobot terkecil, sedangkan prim menghubungkan branch tree secara merambat melalui edge berbobot paling kecil
