# Task 1: Dictionary of Student Marks

student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}
name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")


# Task 2: List Slicing
numbers = list(range(1, 11))
first_five = numbers[:5]
reversed_list = first_five[::-1]

print("Extracted list:", first_five)
print("Reversed list:", reversed_list)
