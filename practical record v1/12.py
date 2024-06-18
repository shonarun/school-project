import pickle

# Function to write student data to file
def write_student_data(filename, student_data):
    with open(filename, 'wb') as file:
        pickle.dump(student_data, file)

# Function to read student data from file
def read_student_data(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Function to update marks based on roll number
def update_marks(filename, roll_no, new_marks):
    student_data = read_student_data(filename)
    found = False
    for student in student_data:
        if student['roll_no'] == roll_no:
            student['marks'] = new_marks
            found = True
            break
    if found:
        write_student_data(filename, student_data)
        print(f"Marks updated for student with roll number {roll_no}.")
    else:
        print(f"Student with roll number {roll_no} not found.")

# Input student data
student_data = [
    {'roll_no': 101, 'name': 'Alice', 'marks': 85},
    {'roll_no': 102, 'name': 'Bob', 'marks': 90},
    {'roll_no': 103, 'name': 'Carol', 'marks': 78},
    {'roll_no': 104, 'name': 'David', 'marks': 92},
    {'roll_no': 105, 'name': 'Eve', 'marks': 88}
]

# Write initial student data to binary file
write_student_data("class.dat", student_data)
print("Initial student data written to class.dat.")

# Update marks based on user input
roll_no = int(input("Enter roll number of student to update marks: "))
new_marks = float(input("Enter new marks: "))

# Call update_marks function to update marks
update_marks("class.dat", roll_no, new_marks)
