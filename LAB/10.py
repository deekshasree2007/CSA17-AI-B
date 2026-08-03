from queue import PriorityQueue

# Input number of vertices
n = int(input("Enter the number of vertices: "))

graph = {}

print("\nEnter the graph details:")

for i in range(n):
    vertex = input("\nEnter vertex: ")
    neighbours = []

    m = int(input(f"Enter number of neighbours of {vertex}: "))

    for j in range(m):
        neighbour = input("Enter neighbour: ")
        cost = int(input(f"Enter cost from {vertex} to {neighbour}: "))
        neighbours.append((neighbour, cost))

    graph[vertex] = neighbours

# Input heuristic values
heuristic = {}

print("\nEnter heuristic values:")

for i in range(n):
    vertex = input("Vertex: ")
    h = int(input(f"Heuristic value of {vertex}: "))
    heuristic[vertex] = h

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

pq = PriorityQueue()
pq.put((heuristic[start], 0, start, [start]))

visited = set()

while not pq.empty():

    f, g, node, path = pq.get()

    if node == goal:
        print("\nGoal Reached!")
        print("Path :", " -> ".join(path))
        print("Total Cost :", g)
        break

    if node not in visited:
        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                pq.put((new_f, new_g, neighbour, path + [neighbour]))
