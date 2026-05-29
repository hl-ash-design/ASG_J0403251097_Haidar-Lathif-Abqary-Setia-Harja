# Nama  : Haidar Lathif Abqary Setia Harja
# NIM   : J0403250197
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree
# ===============================================================
# Studi kasus: Jaringan Kabel Antar Gedung
# ===============================================================

import heapq

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

Denah = {
    'A':[('B',4),('C',2),('D',5)],
    'B':[('A',4),('D',3)],
    'C':[('A',2),('D',1)],
    'D':[('A',5),('B',3),('C',1)]
}

mst, total = prim(Denah, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")

print(f"Total bobot: {total}")

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
# Saat ini, algoritma yang digunakan adalah algoritma prim

# 2. Edge mana saja yang dipilih?
# Edge A-C, C-D, dan D-B

# 3. Berapa total biaya minimum?
# Biaya minimum spanning tree adalah 6

# 4. Mengapa MST cocok digunakan pada kasus ini?
# Karena karena graph MST dapat mencari jalur paling efektif demi meningkatkan efisiensi bahan sekaligus menjaga optimalisasi sistem
