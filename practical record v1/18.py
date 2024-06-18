class Item:
    def __init__(self, item_number, item_name, price):
        self.item_number = item_number
        self.item_name = item_name
        self.price = price

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed Item {item.item_number}: {item.item_name} (${item.price}) to the stack.")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def display(self):
        if not self.is_empty():
            print("\nSTACK CONTENTS:")
            for item in reversed(self.stack):
                print(f"Item Number: {item.item_number}, Item Name: {item.item_name}, Price: ${item.price}")
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

# Function to get item details from user
def get_item_details():
    item_number = input("Enter Item Number: ")
    item_name = input("Enter Item Name: ")
    price = float(input("Enter Price: $"))
    return Item(item_number, item_name, price)

# Main function for menu-driven program
def main():
    stack = Stack()

    while True:
        print("\nSTACK OPERATIONS")
        print("1. Push Item")
        print("2. Pop Item")
        print("3. Display Stack")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = get_item_details()
            stack.push(item)
        elif choice == '2':
            popped_item = stack.pop()
            if popped_item is not None:
                print(f"Popped Item: Item Number {popped_item.item_number}, Item Name {popped_item.item_name}, Price ${popped_item.price}")
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
