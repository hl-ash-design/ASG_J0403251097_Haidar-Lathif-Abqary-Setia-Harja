# Adjacency matrix
def CreateGraph(V, edges):
    graph = [[0 for i in range(V)] for j in range(V)]

    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1
    return graph

if __name__ == "__main__":
    V = 3
    edges = [(0, 1), (1, 2), (0, 2)]
    graph = CreateGraph(V, edges)
    for row in range(V):
        for col in range(V):
            print(graph[row][col], end=" ")
        print()

# Adjacency list
def createGraph(V, edges):
    graph = {i: [] for i in range(V)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

if __name__ == "__main__":
    V = 3
    edges = [(0, 1), (1, 2), (0, 2)]
    graph = createGraph(V, edges)
    for vertex in range(V):
        print(f"Vertex {vertex}: {graph[vertex]}")