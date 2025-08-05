# Define a list with some duplicate elements
numbers = [4, 7, 2, 4, 9, 7, 5, 2, 8, 1, 4]

# Create an empty set to track seen elements and duplicates
seen = set()
duplicates = set()

# Iterate over the list
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

# Print duplicate elements
print("Duplicate elements in the list are:")
for dup in duplicates:
    print(dup)
