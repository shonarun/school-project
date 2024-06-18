def process_numbers(numbers_list):
    modified_list = []
    for num in numbers_list:
        if num % 2 == 0:
            # If the number is even, halve it
            modified_list.append(num / 2)
        else:
            # If the number is odd, double it
            modified_list.append(num * 2)
    return modified_list

# Get input from the user
numbers_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Call the function and display the result
modified_list = process_numbers(numbers_list)
print("The modified list is:", modified_list)
