# Creating a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

# Taking input from the user
student_name = input("Enter the student's name: ")

# Checking if the student exists in the dictionary
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not Found.")