# Depth First Search (DFS)

# Function for DFS
def dfs(vertex, graph, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(neighbour, graph, visited)

# Input number of vertices
n = int(input("Enter number of vertices: "))

graph = {}

# Input graph
for i in range(n):
    vertex = input("\nEnter vertex: ")
    neighbours = input(f"Enter neighbours of {vertex} (space-separated): ").split()
    graph[vertex] = neighbours

# Input starting vertex
start = input("\nEnter starting vertex: ")

visited = set()

print("\nDFS Traversal:")
dfs(start, graph, visited)
