from collections import deque

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Find the blank space (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Convert list to tuple (for visited)
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            # Swap blank with adjacent tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors

# BFS Algorithm
def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        state_tuple = to_tuple(state)

        if state_tuple not in visited:
            visited.add(state_tuple)

            for neighbor in get_neighbors(state):
                queue.append((neighbor, path + [state]))

    return None

# Print puzzle
def print_puzzle(state):
    for row in state:
        print(row)
    print()

# User input
print("Enter the initial puzzle (use 0 for blank):")

start = []
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

solution = bfs(start)

if solution:
    print("\nSolution Found!\n")
    for step in solution:
        print_puzzle(step)
else:
    print("No solution exists.")
