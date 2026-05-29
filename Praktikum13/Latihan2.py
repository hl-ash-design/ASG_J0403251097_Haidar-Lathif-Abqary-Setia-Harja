# Nama  : Haidar Lathif Abqary Setia Harja
# NIM   : J0403250197
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree
# ===============================================================
# Implementasi Sederhana Algoritma Kruskal
# ===============================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()
print(edges)

# Menyiapkan mst
mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # mendata edge dan bobot tree
        mst.append((u, v, weight))
        total_weight += weight

        # mendata verteks yang sudah dilewati
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")

print(f"Total Weight: {total_weight}")

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
# Edge dengan bobot paling kecil

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# Karena pembuatan MST metode kruskal mengutamakan edge dengan bobot paling kecil demi mengoptimalkan bobot tree

# 3. Berapa total bobot MST yang dihasilkan?
# Total bobot tree adalah 6

# 4. Mengapa edge tertentu tidak dipilih?
# Karena edge tersebut sudah terhubung dengan tree dan demi menghindari loop
