def search_element(numbers_list, element):
    locations = [index for index, num in enumerate(numbers_list) if num == element]
    frequency = len(locations)
    return locations, frequency

# Get input from the user
numbers_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
element_to_search = int(input("Enter the element to search for: "))

# Call the function and display the result
locations, frequency = search_element(numbers_list, element_to_search)

if frequency > 0:
    print(f"The element {element_to_search} is found at locations: {locations}")
    print(f"The frequency of the element {element_to_search} is: {frequency}")
else:
    print(f"The element {element_to_search} is not found in the list.")
