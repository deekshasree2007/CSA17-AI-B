from itertools import permutations

# Input number of cities
n = int(input("Enter the number of cities: "))

# Input cost matrix
cost = []

print("Enter the cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

cities = list(range(1, n))

min_cost = float('inf')
best_path = []

# Find minimum cost tour
for path in permutations(cities):
    current_cost = 0
    current_city = 0

    for city in path:
        current_cost += cost[current_city][city]
        current_city = city

    current_cost += cost[current_city][0]

    if current_cost < min_cost:
        min_cost = current_cost
        best_path = (0,) + path + (0,)

# Display result
print("\nMinimum Cost:", min_cost)

print("Best Path:", end=" ")
for city in best_path:
    print(city, end=" ")
