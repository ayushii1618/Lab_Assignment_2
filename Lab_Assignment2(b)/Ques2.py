# Create a tuple of 5 students
students = ("Ayushi", "Rohan", "Sneha", "Amit", "Neha")

# a. Display all the students
print("a. All students:", students)

# b. Add a new student (tuples are immutable, so we create a new tuple)
new_student = "Kabir"
students = students + (new_student,)
print("b. After adding a new student:", students)

# c. Delete a student (tuples are immutable, so convert to list first)
students_list = list(students)
students_list.remove("Amit")  # removing one student
students = tuple(students_list)
print("c. After deleting a student:", students)

# d. Use slicing to print students from the first index to third index
print("d. Students from index 1 to 3:", students[1:4])

# e. Modify the second index value
try:
    students[2] = "Tanvi"  # Attempting to modify index 2
except TypeError as e:
    print("e. Error: Tuples are immutable, so you can't modify elements!")
    print("   Exception message:", e)
