def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_vowels_consonants_digits(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    digits = "0123456789"

    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    digit_count = sum(1 for char in text if char in digits)

    return vowel_count, consonant_count, digit_count

# Input text to write to the file
poem_content = """
This is a sample poem.
It has some words and numbers 123.
We will count vowels, consonants and digits in this poem.
"""

# Write to file
write_to_file("poem.txt", poem_content)

# Read from file
file_content = read_file("poem.txt")

# Count vowels, consonants, and digits
vowel_count, consonant_count, digit_count = count_vowels_consonants_digits(file_content)

# Display counts
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
print(f"Number of digits: {digit_count}")
