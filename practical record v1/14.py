import csv

# Function to insert records into books.csv
def insert_records(filename, records):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)
    print(f"Records inserted into {filename} successfully.")

# Function to display records from books.csv
def display_records(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        print("\nBOOKS LIST:")
        for row in reader:
            print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Price: ${row[3]}")

# Main function for the program
def main():
    books_data = []

    while True:
        print("\nINSERT BOOK RECORD")
        bookid = input("Enter Book ID (press Enter to stop): ")
        if not bookid:
            break
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        price = input("Enter Price: $")
        books_data.append([bookid, title, author, price])

    insert_records("books.csv", books_data)
    display_records("books.csv")

if __name__ == "__main__":
    main()
