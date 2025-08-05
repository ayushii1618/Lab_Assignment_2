# File name (make sure this file exists or will be created in the same directory)
filename = "my_file.txt"

# New content to write
new_content = "Hi, I am currently pursuing my BTech from Jaypee."

# Open the file in write mode to replace content
with open(filename, "w") as file:
    file.write(new_content)

print("File content replaced successfully.")
