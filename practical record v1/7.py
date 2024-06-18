def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_and_replace(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
        modified_content = file_content.replace(' ', '#')
        return modified_content

# Input text to write to the file
text_to_write = input("Enter text to write to Notes.txt: ")

# Write to file
write_to_file("Notes.txt", text_to_write)

# Read from file, replace spaces with #
modified_text = read_and_replace("Notes.txt")

# Display modified content
print("Modified content:")
print(modified_text)
