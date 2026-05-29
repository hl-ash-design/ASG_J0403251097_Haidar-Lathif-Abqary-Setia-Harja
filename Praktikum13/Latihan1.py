# Nama  : Haidar Lathif Abqary Setia Harja
# NIM   : J0403250197
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree
# ===============================================================
# Implementasi Spanning Tree Sederhana
# ===============================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('A', 'D')
]

# Spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menammpilkan edge pada graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan graph dalam bentuk tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge pada graph:", len(edges))
print("Jumlah edge pada spanning tree:", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# Graph spanning tree memiliki lebih sedikit edges dibandingkan dengan graph awal

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Karena demi menghindari adanya fenomena branch menjadi root akan dirinya sendiri

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Karena spanning tree mengambil jalur paling efisien yang terdiri dari satu jalur