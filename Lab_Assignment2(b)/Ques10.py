# Define a list of numbers
numbers = [10, 15, 22, 33, 47, 50, 61, 72, 85]

# Use list comprehension to get only odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the result
print("Odd numbers in the list:", odd_numbers)
