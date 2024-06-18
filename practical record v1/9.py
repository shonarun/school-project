def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def find_four_letter_words(text):
    words = text.split()
    four_letter_words = [word for word in words if len(word) == 4]
    return four_letter_words

# Input text to write to the file
notes_content = """
This is a sample text file.
It contains some four letter words like this, test, word, and also some longer words.
We will extract only the four letter words from this file.
"""

# Write to file
write_to_file("Notes.txt", notes_content)

# Read from file
file_content = read_file("Notes.txt")

# Find and display four letter words
four_letter_words = find_four_letter_words(file_content)

print("Four letter words in Notes.txt:")
for word in four_letter_words:
    print(word)
