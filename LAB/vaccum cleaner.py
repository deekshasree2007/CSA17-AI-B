# Vacuum Cleaner Problem

# Input number of rooms
n = int(input("Enter number of rooms: "))

rooms = []

# Input state of each room
for i in range(n):
    state = input(f"Enter state of Room {i+1} (Dirty/Clean): ").strip().lower()
    rooms.append(state)

# Input starting room
position = int(input(f"Enter starting room (1-{n}): ")) - 1

print("\nVacuum Cleaner Started...\n")

visited = 0

while visited < n:
    if rooms[position] == "dirty":
        print(f"Room {position+1} is Dirty.")
        print(f"Cleaning Room {position+1}...")
        rooms[position] = "clean"
    else:
        print(f"Room {position+1} is already Clean.")

    visited += 1

    if visited < n:
        position = (position + 1) % n
        print(f"Moving to Room {position+1}...\n")

print("\nFinal State of Rooms:")
for i in range(n):
    print(f"Room {i+1}: {rooms[i].capitalize()}")

print("\nAll rooms are Clean.")
