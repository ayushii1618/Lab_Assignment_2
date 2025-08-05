# Create a dictionary with name as key and age as value
students = {
    "Ayushi": 19,
    "Rohan": 21,
    "Sneha": 22,
    "Amit": 18,
    "Neha": 20
}

# a. Display students whose age is greater than 20
print("a. Students with age > 20:")
for name, age in students.items():
    if age > 20:
        print(f"   {name}: {age}")

# b. Add one more student with age 30
students["Kabir"] = 30
print("\nb. After adding Kabir (age 30):")
print(students)

# c. Display all students using .items()
print("\nc. All students using .items():")
for name, age in students.items():
    print(f"   {name}: {age}")

# d. Delete a student
del students["Amit"]
print("\nd. After deleting 'Amit':")
print(students)

# e. Display the average age of all the students
total_age = sum(students.values())
average_age = total_age / len(students)
print(f"\ne. Average age of all students: {average_age:.2f}")
