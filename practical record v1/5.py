def sum_key_value_pairs(input_dict):
    sums_list = [key + value for key, value in input_dict.items()]
    return sums_list

# Get input from the user
input_str = input("Enter dictionary items in the format 'key1:value1, key2:value2, ...': ")

# Convert input string to dictionary
input_dict = dict(item.split(":") for item in input_str.split(", "))
input_dict = {int(k): int(v) for k, v in input_dict.items()}

# Call the function and display the result
sums_list = sum_key_value_pairs(input_dict)
print("The sum of key:value pairs is:", sums_list)
