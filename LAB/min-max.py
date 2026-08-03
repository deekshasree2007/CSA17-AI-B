import math

# Minimax Function
def minimax(depth, node, maximizing, values, height):

    # If leaf node is reached
    if depth == height:
        return values[node]

    if maximizing:
        best = -math.inf

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, False, values, height)
            best = max(best, value)

        return best

    else:
        best = math.inf

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i, True, values, height)
            best = min(best, value)

        return best


# ---------------- Main Program ----------------

height = int(input("Enter the height of the game tree: "))

leaf_nodes = 2 ** height

print("Enter", leaf_nodes, "leaf node values:")

values = list(map(int, input().split()))

result = minimax(0, 0, True, values, height)

print("\nOptimal Value:", result)
