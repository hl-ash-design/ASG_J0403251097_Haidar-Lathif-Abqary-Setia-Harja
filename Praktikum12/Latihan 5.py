# Nama  : Haidar Lathif Abqary Setia Harja
# NIM   : J0403250197
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path
graph = {
    "Bogor":{"Jakarta":5, "Depok": 2},
    "Depok":{"Jakarta":2, "Bandung": 6},
    "Jakarta":{"Bandung":7},
    "Bandung":{}
}

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

hasil = dijkstra(graph,"Bogor")
print("Lokasi terdekat dari Bogor:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "jam")
# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
'''Node Bogor'''
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
'''Node Depok'''
# 3. Node mana yang memiliki jarak paling besar dari node awal?
'''Node Bandung'''
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
'''algoritma Dijkstra bekerja dengan memetakan edge node dari bobot yang paling kecil'''
