# File from Question 6
filename = "my_file.txt"

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        content = file.read()

    # Count characters
    char_count = len(content)

    # Display the result
    print(f"Total number of characters in '{filename}':", char_count)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
