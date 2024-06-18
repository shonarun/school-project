import csv

# Function to insert user-id and password into user_passwords.csv
def insert_records(filename, records):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        for record in records:
            writer.writerow(record)
    print(f"Records inserted into {filename} successfully.")

# Function to search for password based on user-id
def search_password(filename, userid):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == userid:
                return row[1]
    return None

# Input user-id and password records
def input_user_password_records():
    records = []
    while True:
        userid = input("Enter user ID (press Enter to stop): ")
        if not userid:
            break
        password = input("Enter password: ")
        records.append([userid, password])
    return records

# Input user-id and password records and insert into user_passwords.csv
user_password_records = input_user_password_records()
insert_records("user_passwords.csv", user_password_records)

# Search for password based on user-id
search_userid = input("Enter user ID to search: ")
found_password = search_password("user_passwords.csv", search_userid)

# Display result based on search
if found_password:
    print(f"Password found! Password for user ID {search_userid}: {found_password}")
else:
    print(f"Password not found for user ID {search_userid}.")
