import os

# Data to store in library
LIBRARY_FILE = "library.txt"

# Initoializing Library
library = []

def load_library():
    """Load library data from a file."""
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            for line in file:
                title, author, year, genre, read_status = line.strip().split("|")
                library.append({
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "genre": genre,
                    "read_status": read_status == "True"
                })
        print("Library loaded successfully!")
    else:
        print("No existing library found. Starting with an empty library.")

# Save Book Functionality
def save_library():
    """Save library data to a file."""
    with open(LIBRARY_FILE, "w") as file:
        for book in library:
            file.write(f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{book['read_status']}\n")
    print("Library saved successfully!")

# Add Book Functionality
def add_book():
    """Add a new book to the library."""
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    library.append(book)
    print(f"Book '{title}' added successfully!")

# Remove Book Functionality
def remove_book():
    """Remove a book from the library by title."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed successfully!")
            return
    print(f"Book '{title}' not found in the library.")

# Search Book Functionality
def search_book():
    """Search for a book by title."""
    title = input("Enter the title of the book to search: ")
    for book in library:
        if book["title"].lower() == title.lower():
            print("\nBook Found:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Read Status: {'Read' if book['read_status'] else 'Unread'}")
            return
    print(f"Book '{title}' not found in the library.")

# Display All Book Functionality
def display_all_books():
    """Display all books in the library."""
    if not library:
        print("The library is empty.")
        return
    
    print("\nAll Books in Library:")
    for book in library:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Publication Year: {book['year']}")
        print(f"Genre: {book['genre']}")
        print(f"Read Status: {'Read' if book['read_status'] else 'Unread'}")
        print("-" * 30)

# Statics 
def display_statistics():
    """Display library statistics."""
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return
    
    read_books = sum(book["read_status"] for book in library)
    percentage_read = (read_books / total_books) * 100
    
    print("\nLibrary Statistics:")
    print(f"Total Books: {total_books}")
    print(f"Percentage Read: {percentage_read:.2f}%")

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    load_library()
    main_menu()