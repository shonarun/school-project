import pickle

# Function to write employee data to binary file
def write_employee_data(filename, employee_data):
    with open(filename, 'wb') as file:
        pickle.dump(employee_data, file)

# Function to read employee data from binary file
def read_employee_data(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Function to delete employees with salary > 25000
def delete_high_salary_employees(filename):
    employee_data = read_employee_data(filename)
    updated_data = [emp for emp in employee_data if emp['salary'] <= 25000]
    write_employee_data(filename, updated_data)
    print("Employees with salary greater than 25000 deleted successfully.")

# Initial data for employees
employee_data = [
    {'empid': 101, 'empname': 'Alice', 'salary': 22000},
    {'empid': 102, 'empname': 'Bob', 'salary': 27000},
    {'empid': 103, 'empname': 'Carol', 'salary': 24000}
]

# Write initial employee data to binary file
write_employee_data("emp.dat", employee_data)
print("Initial employee data written to emp.dat.")

# Delete employees with salary > 25000
delete_high_salary_employees("emp.dat")
