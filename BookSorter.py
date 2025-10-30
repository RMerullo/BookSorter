from array import array

file_path = "lovahs_books.txt"
book_array = list()
sorted_by_title = list()
try:
    with open(file_path, 'r') as file:
        content = file.read().splitlines()
        print(f"Content: {content}")
        book_array.append(content);
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"Book Array: {book_array}")
print(f"Sorted Book Array: {book_array.sort}")

# with open("Sorted_Books.txt", "w") as new_file:
#   for book in sorted(book_array):
#     new_file.write(book)