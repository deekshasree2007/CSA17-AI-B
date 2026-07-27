from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque()

    # Initial state: both jugs are empty
    queue.append(((0, 0), []))

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Check if target is reached
        if x == target or y == target:
            print("\nSolution Found!\n")
            for state in path:
                print(state)
            return

        # Generate all possible next states
        next_states = [
            (jug1, y),   # Fill Jug 1
            (x, jug2),   # Fill Jug 2
            (0, y),      # Empty Jug 1
            (x, 0),      # Empty Jug 2

            # Pour Jug 1 -> Jug 2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),

            # Pour Jug 2 -> Jug 1
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    print("\nNo solution is possible.")

# -------- Main Program --------

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if target > max(jug1, jug2):
    print("Target cannot be greater than both jug capacities.")
else:
    water_jug_bfs(jug1, jug2, target)
