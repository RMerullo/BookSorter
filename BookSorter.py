from array import array

# Books in text file are formatted as:
# Title | Author

file_path = "books_unsorted.txt"
book_array = list()
try:
    with open(file_path, 'r') as file:
        for line in file:
            currentLine = line.rstrip()
            currentLine.replace("\n","")
            content = currentLine.split('|')
            # Entry was not formatted correctly
            if(len(content) != 2):
               raise ValueError("The following entry is not formatted correctly: \n" + content[0])
            book_array.append(content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Sort books by title and write to file
with open("SortedByTitle.txt", "w") as new_file:
  for book in sorted(book_array):
    new_file.write(book[0] + " by " + book[1])
    new_file.write("\n")

# Sort books by author and write to file
books_sorted_by_title = list()
for book in book_array:
    books_sorted_by_title.append(book[1] + " | " + book[0])
with open("SortedByAuthor.txt", "w") as new_file:
    for book in sorted(books_sorted_by_title):
        new_file.write(book)
        new_file.write("\n")

print(f"Success!")