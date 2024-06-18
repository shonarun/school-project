import csv

# Function to insert records into exams.csv
def insert_records(filename, records):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        for record in records:
            writer.writerow(record)
    print(f"Records inserted into {filename} successfully.")

# Function to display records with rank less than 10
def display_records_less_than_10(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header line
        print(f"\nRecords with rank less than 10 from {filename}:")
        for row in reader:
            studentid, name, rank = row
            if int(rank) < 10:
                print(f"Student ID: {studentid}, Name: {name}, Rank: {rank}")

# Input student records
def input_student_records():
    records = []
    while True:
        studentid = input("Enter student ID (press Enter to stop): ")
        if not studentid:
            break
        name = input("Enter student name: ")
        rank = input("Enter student rank: ")
        records.append([studentid, name, rank])
    return records

# Input student records and insert into exams.csv
student_records = input_student_records()
insert_records("exams.csv", student_records)

# Display records with rank less than 10 from exams.csv
display_records_less_than_10("exams.csv")
