# Nama  : Haidar Lathif Abqary Setia Harja
# NIM   : J0403250197
# Kelas : A2
# Praktikum 13 - Graph III: Minimum Spanning Tree
# ===============================================================
# Implementasi Kruskal
# ===============================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot
edges.sort()

mst = []
total_weight = 0

# Set sederhana untuk node yang sudah dipilih
connected_nodes = set()

for weight, u, v in edges:

    # Jika edgetidak membentuk xyxle sederhana
    if u not in connected_nodes or v not in connected_nodes:

        mst.append((u, v, weight))
        total_weight += weight

        connected_nodes.add(u)
        connected_nodes.add(v)

print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")

print(f"Total Bobot MST: {total_weight}")