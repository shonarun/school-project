def count_odd_even(numbers_tuple):
    odd_count = 0
    even_count = 0
    for num in numbers_tuple:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count

# Get input from the user
numbers_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
numbers_tuple = tuple(numbers_list)

# Call the function and display the result
odd_count, even_count = count_odd_even(numbers_tuple)
print(f"The count of odd numbers is: {odd_count}")
print(f"The count of even numbers is: {even_count}")
