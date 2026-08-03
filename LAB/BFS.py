from collections import deque

# Input number of vertices
n = int(input("Enter number of vertices: "))

graph = {}

# Input adjacency list
for i in range(n):
    vertex = input("\nEnter vertex: ")
    neighbours = input(f"Enter neighbours of {vertex} (space-separated): ").split()
    graph[vertex] = neighbours

# Input starting vertex
start = input("\nEnter starting vertex: ")

visited = set()
queue = deque()

queue.append(start)
visited.add(start)

print("\nBFS Traversal:")

while queue:
    vertex = queue.popleft()
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
