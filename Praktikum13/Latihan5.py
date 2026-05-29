# Nama  : Haidar Lathif Abqary Setia Harja
# NIM   : J0403250197
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree
# ===============================================================
# Program MST dengan Kasus Baru
# ===============================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

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
# 1. Kasus apa yang dipilih?
# Kasus jaringan jalan antar kota

# 2. Algoritma apa yang digunakan?
# Algoritma kruskal

# 3. Edge mana saja yang dipilih dalam MST?
# Edge Bogor-Depok, Depok-Jakarta, dan Jakarta-Bandung

# 4. Berapa total bobot MST?
# TOtal bobot MST adalah 9

# 5. Mengapa edge tertentu tidak dipilih?
# Karena ukuran file input yang relatif besar