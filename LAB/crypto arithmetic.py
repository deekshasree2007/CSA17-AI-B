from itertools import permutations

def solve_cryptarithm(expression):
    expression = expression.replace(" ", "")

    # Split into left and right side
    left, right = expression.split("=")
    words = left.split("+")

    # Get unique letters
    letters = []
    for ch in expression:
        if ch.isalpha() and ch not in letters:
            letters.append(ch)

    if len(letters) > 10:
        print("More than 10 unique letters. No solution possible.")
        return

    # First letters cannot be zero
    first_letters = set(word[0] for word in words + [right])

    digits = "0123456789"

    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Skip if any first letter is zero
        if any(mapping[ch] == '0' for ch in first_letters):
            continue

        # Convert words to numbers
        nums = [int("".join(mapping[ch] for ch in word)) for word in words]
        result = int("".join(mapping[ch] for ch in right))

        if sum(nums) == result:
            print("\nSolution Found!\n")
            for letter in sorted(mapping):
                print(f"{letter} = {mapping[letter]}")

            print("\nVerification:")
            for word, num in zip(words, nums):
                print(f"{word} = {num}")
            print(f"{right} = {result}")
            return

    print("No solution found.")

# ---------------- Main Program ----------------
expr = input("Enter cryptarithm (Example: SEND+MORE=MONEY): ")
solve_cryptarithm(expr)
