import pickle

def write_student_data(filename, student_data):
    with open(filename, 'wb') as file:
        pickle.dump(student_data, file)

def search_student_by_rollno(filename, roll_no):
    with open(filename, 'rb') as file:
        student_data = pickle.load(file)
        for student in student_data:
            if student['roll_no'] == roll_no:
                return student['name']
        return None

# Function to input student data
def input_student_data():
    student_data = []
    for i in range(5):
        roll_no = int(input(f"Enter roll number for student {i+1}: "))
        name = input(f"Enter name for student {i+1}: ")
        student_data.append({'roll_no': roll_no, 'name': name})
    return student_data

# Input student data
student_data = input_student_data()

# Write student data to binary file
write_student_data("student.dat", student_data)
print("Student data written to student.dat.")

# Search for a student by roll number
search_roll_no = int(input("Enter roll number to search: "))
found_name = search_student_by_rollno("student.dat", search_roll_no)

# Display result based on search
if found_name:
    print(f"Student found! Name: {found_name}")
else:
    print("Student not found with that roll number.")
