# reverse.py

# Specify the filename to read from
filename = "example.txt"  # Make sure this file exists in the same directory

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        lines = file.readlines()

    # Print lines in reverse order
    print("Lines in reverse order:\n")
    for line in reversed(lines):
        print(line.strip())

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
