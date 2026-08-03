from collections import deque

# Input from user
n = int(input("Enter the number of Missionaries: "))
c = int(input("Enter the number of Cannibals: "))

# Check valid state
def is_valid(m_left, c_left):
    m_right = n - m_left
    c_right = c - c_left

    if m_left < 0 or c_left < 0 or m_left > n or c_left > c:
        return False

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True

moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]

start = (n, c, 1)
goal = (0, 0, 0)

queue = deque([(start, [start])])
visited = set()

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("\nSolution Path:")
        for s in path:
            side = "Left" if s[2] == 1 else "Right"
            print(f"Missionaries Left = {s[0]}, Cannibals Left = {s[1]}, Boat = {side}")
        break

    if state in visited:
        continue

    visited.add(state)

    m, ca, boat = state

    for dm, dc in moves:
        if boat == 1:
            new_state = (m - dm, ca - dc, 0)
        else:
            new_state = (m + dm, ca + dc, 1)

        if is_valid(new_state[0], new_state[1]):
            queue.append((new_state, path + [new_state]))
else:
    print("No Solution Exists")
