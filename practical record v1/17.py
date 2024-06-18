class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def display(self):
        if not self.is_empty():
            print("Stack contents:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

# Function to push numbers divisible by 5 into stack
def push_divisible_by_5(numbers, stack):
    for num in numbers:
        if num % 5 == 0:
            stack.push(num)

# Main function for menu-driven program
def main():
    stack = Stack()
    numbers = [12, 15, 25, 30, 18, 10, 20]

    push_divisible_by_5(numbers, stack)

    while True:
        print("\nSTACK OPERATIONS")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = int(input("Enter number to push: "))
            stack.push(item)
        elif choice == '2':
            popped_item = stack.pop()
            if popped_item is not None:
                print(f"Popped item: {popped_item}")
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
