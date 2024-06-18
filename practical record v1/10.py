def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_and_display_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip().startswith('T'):
                print(line.strip())

# Input text to write to the file
article_content = """
This is an article.
It contains some lines starting with different letters.
Some lines start with T, others start with S or A.
We will display only the lines that start with T.
"""

# Write to file
write_to_file("article.txt", article_content)

# Read from file and display lines starting with 'T'
print("Lines from article.txt starting with 'T':")
read_and_display_lines("article.txt")
