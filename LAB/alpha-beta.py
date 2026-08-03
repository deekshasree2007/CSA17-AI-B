MIN = -1000
MAX = 1000

# Alpha-Beta Function
def alpha_beta(depth, node, maximizing, values, alpha, beta, height):

    # Leaf node reached
    if depth == height:
        return values[node]

    if maximizing:
        best = MIN

        for i in range(2):
            value = alpha_beta(depth + 1,
                               node * 2 + i,
                               False,
                               values,
                               alpha,
                               beta,
                               height)

            best = max(best, value)
            alpha = max(alpha, best)

            # Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for i in range(2):
            value = alpha_beta(depth + 1,
                               node * 2 + i,
                               True,
                               values,
                               alpha,
                               beta,
                               height)

            best = min(best, value)
            beta = min(beta, best)

            # Pruning
            if beta <= alpha:
                break

        return best


# ---------------- Main Program ----------------

height = int(input("Enter the height of the game tree: "))

leaf_nodes = 2 ** height

print("Enter", leaf_nodes, "leaf node values:")

values = list(map(int, input().split()))

result = alpha_beta(0, 0, True, values, MIN, MAX, height)

print("\nOptimal Value:", result)
